import tkinter as tk
import random

window=tk.Tk()

label1=tk.Label(window,text=" ",bg="green",width=15)
label1.pack()

def r():
    random1=random.randint(1,10)
    label1.config(text=random1)
    
button1=tk.Button(text="click",bg="yellow",command=r)
button1.pack()

tk.mainloop()

