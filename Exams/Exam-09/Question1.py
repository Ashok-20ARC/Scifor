import tkinter as tk
from tkinter import scrolledtext,messagebox
import requests

url="https://jsonplaceholder.typicode.com/posts"

def make_request(method):
    try:
        post_id=entry_id.get()
        data={
            "title":entry_title.get(),
            "body":entry_body.get(),
            "userId":1
        }

        if method=="GET":
            response=requests.get(f"{url}/{post_id}" if post_id else url)
        
        elif method=="POST":
            response=requests.post(url,json=data)
        
        elif method=="PUT":
            if not post_id:
                messagebox.showwarning("Warning","ID not found for PUT request")
                return
            response=requests.put(f"{url}/{post_id}",json=data)

        elif method=="DELETE":
            if not post_id:
                messagebox.showwarning("Warning","ID not found for DELETE request")
                return
            response=requests.delete(f"{url}/{post_id}")
            
        text_response.delete(1.0,tk.END)
        text_response.insert(tk.END,response.json())

    except Exception as e:
        messagebox.showerror("Error",str(e))

root=tk.Tk()
root.title("REST API Methods")
root.geometry('500x500')

tk.Label(root,text="Post ID:").pack()
entry_id=tk.Entry(root)
entry_id.pack()

tk.Label(root,text="Title:").pack()
entry_title=tk.Entry(root)
entry_title.pack()

tk.Label(root,text="Body:").pack()
entry_body=tk.Entry(root)
entry_body.pack()

tk.Button(root,text="GET",command=lambda:make_request("GET")).pack()
tk.Button(root,text="POST",command=lambda:make_request("POST")).pack()
tk.Button(root,text="PUT",command=lambda:make_request("PUT")).pack()
tk.Button(root,text="DELETE",command=lambda:make_request("DELETE")).pack()

text_response=scrolledtext.ScrolledText(root,height=10)
text_response.pack(fill=tk.BOTH,expand=True)

root.mainloop()