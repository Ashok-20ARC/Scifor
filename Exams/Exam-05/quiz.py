import tkinter as tk
from tkinter import messagebox

questions=[
    {"question":"What is the capital of France?",
     "options":["Paris","London","Berlin","Madrid"],
     "answer":"Paris"},
    {"question":"What is 5 + 3?",
     "options":["5","8","10","15"],
     "answer":"8"},
    {"question":"Which programming language is known for AI?",
     "options":["Python","C","HTML","Java"],
     "answer":"Python"},
    {"question":"What does CPU stands for?",
     "options":["Central Proccessing Unit","Computer Personal Unit","Central Personal Unit","Central Programming Unit"],
     "answer":"Central Proccessing Unit"},
    {"question":"What does HTML stand for?",
     "options":["Hyper Text Markup Language","High Text Machine Language","Hyper Text Machine Language","High Task Machine Language"],
     "answer":"Hyper Text Markup Language"},
    {"question":"Which animal is known as the king of the Jungle?",
     "options":["Tiger","Elephant","Lion","Cheetah"],
     "answer":"Lion"},
    {"question":"What is the square root of 64?",
     "options":["6","8","7","10"],
     "answer":"8"},
    {"question":"Which organ is responsible for pumping Blood?",
     "options":["Lungs","Heart","Liver","Brain"],
     "answer":"Heart"},
    {"question":"What is the chemical symbol for water?",
     "options":["O2","H2O","CO2","H2"],
     "answer":"H2O"},
    {"question":"What is the largest planet in the solar system?",
     "options":["Earth","Jupiter","Mars","Saturn"],
     "answer":"Jupiter"}
    ]

current_question=0
score=0

def check_answer(selected_option):
    global current_question,score
    
    if selected_option==questions[current_question]["answer"]:
        score+=1
    current_question+=1
    
    if current_question<len(questions):
        display_question()
    else:
        show_score()

def display_question():
    global current_question
    
    question_label.config(text=questions[current_question]["question"])
    
    for i,option in enumerate(questions[current_question]["options"]):
        option_buttons[i].config(text=option,command=lambda opt=option:check_answer(opt))

def show_score():
    messagebox.showinfo("Quiz Completed",f"Your final score is {score}/{len(questions)}")
    root.destroy()

root=tk.Tk()
root.title("Quiz Application")
root.geometry("500x500")
root.configure(bg="#2E2E2E")

question_label=tk.Label(root,text="",wraplength=350,font=("Arial",14),justify="center",bg="#2E2E2E",fg="#FFFFFF")
question_label.pack(pady=20)

option_buttons=[]

for i in range(4):
    button=tk.Button(root,text="",width=30,font=("Arial",12),bg="#4F4F4F",fg="#FFFFFF",activebackground="#6F6F6F",activeforeground="#FFFFFF")
    button.pack(pady=5)
    option_buttons.append(button)

display_question()

root.mainloop()