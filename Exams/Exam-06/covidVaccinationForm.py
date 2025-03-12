import tkinter as tk
from tkinter import messagebox

class VaccinationForm:
    def __init__(self,root):
        self.root=root
        self.root.title("COVID-19 VACCINATION FORM")
        self.root.geometry("400x500")
        
        self.root.configure(bg="#2C2F33")
        
        tk.Label(root,text="COVID-19 VACCINATION FORM",font=("Arial",16,"bold"),bg="#2C2F33",fg="#FFFFFF").grid(row=0,column=0,columnspan=2,pady=10)
        
        tk.Label(root,text="Name :",bg="#2C2F33",fg="#FFFFFF").grid(row=1,column=0,sticky='e',padx=10,pady=5)
        self.name_entry=tk.Entry(root,width=30,bg="#23272A",fg="#FFFFFF",insertbackground="#FFFFFF")
        self.name_entry.grid(row=1,column=1,padx=10,pady=5)
        
        tk.Label(root,text="Age     :",bg="#2C2F33",fg="#FFFFFF").grid(row=2,column=0,sticky='e',padx=10,pady=5)
        self.age_entry=tk.Entry(root,width=30,bg="#23272A",fg="#FFFFFF",insertbackground="#FFFFFF")
        self.age_entry.grid(row=2,column=1,padx=10,pady=5)
        
        tk.Label(root,text="Gender :",bg="#2C2F33",fg="#FFFFFF").grid(row=3,column=0,sticky='e',padx=10,pady=5)
        self.gender_var=tk.StringVar(value="Select")
        tk.OptionMenu(root,self.gender_var,"Male","Female","Other").config(bg="#23272A",fg="#FFFFFF",activebackground="#99AAB5")
        tk.OptionMenu(root,self.gender_var,"Male","Female","Other").grid(row=3,column=1,padx=10,pady=5,sticky='w')
        
        tk.Label(root,text="Vaccine\nType   :",bg="#2C2F33",fg="#FFFFFF").grid(row=4,column=0,sticky='e',padx=10,pady=5)
        self.vaccine_var=tk.StringVar(value="Select")
        tk.OptionMenu(root, self.vaccine_var, "Covaxin", "Covishield").config(bg="#23272A",fg="#FFFFFF",activebackground="#99AAB5")
        tk.OptionMenu(root, self.vaccine_var, "Covaxin", "Covishield").grid(row=4,column=1,padx=10,pady=5,sticky='w')
        
        tk.Label(root,text="Dose    :",bg="#2C2F33",fg="#FFFFFF").grid(row=5,column=0,sticky='e',padx=10,pady=5)
        self.dose_var=tk.StringVar(value="Select")
        tk.OptionMenu(root, self.dose_var, "1st Dose","2nd Dose", "Booster").config(bg="#23272A",fg="#FFFFFF",activebackground="#99AAB5")
        tk.OptionMenu(root, self.dose_var, "1st Dose", "2nd Dose","Booster").grid(row=5,column=1,padx=10,pady=5,sticky='w')

        tk.Label(root,text="Address :",bg="#2C2F33",fg="#FFFFFF").grid(row=6,column=0,sticky='ne',padx=10,pady=5)
        self.address_entry=tk.Text(root,width=30,height=5,bg="#23272A",fg="#FFFFFF",insertbackground="#FFFFFF")
        self.address_entry.grid(row=6,column=1,padx=10,pady=5)
        
        tk.Button(root,text="Submit",command=self.submit_form,bg="#7289DA",fg="#FFFFFF",activebackground="#99AAB5").grid(row=7,column=0,columnspan=2,pady=10)
        
    def submit_form(self):
        name=self.name_entry.get()
        age=self.age_entry.get()
        gender=self.gender_var.get()
        vaccine_type=self.vaccine_var.get()
        dose=self.dose_var.get()
        address=self.address_entry.get("1.0",tk.END).strip()
            
        if not name or not age or gender=="Select" or vaccine_type == "Select" or dose=="Select" or not address:
            messagebox.showerror("Error","All fields are required!")
        
        elif not age.isdigit() or int(age)<=0:
            messagebox.showinfo("Error","Age must be a valid positive number!")
        
        else:
            messagebox.showinfo("Success",f"Form submitted successfully!\n\nName: {name}\nAge: {age}\nGender: {gender}\nVaccine: {vaccine_type}\nDose: {dose}\nAddress: {address}")
        
root=tk.Tk()
app=VaccinationForm(root)
root.mainloop()