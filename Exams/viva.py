import requests
import tkinter as tk
import random

root=tk.Tk()

def data():
    Id=random.randint(1,100)
    print(Id)
    url=f"https://jsonplaceholder.typicode.com/posts/{Id}"
    
    response=requests.get(url)
    j_data=response.json()
    
    title=j_data.get('title','no title found')
    body=j_data.get('body','no body found')
    
    label.config(text=f"Id : {Id}\n\nTitle : {title}\n\n Body : {body}")
    
root.title("Data Fetching using request")
root.geometry("500x500")

label=tk.Label(root,text="data will be display here",font=("Arial",16),wraplength=1000)
label.pack(pady=20)

button=tk.Button(root,text="click here to fetch data",command=data,font=("Arial",16))
button.pack()

root.mainloop()    
    