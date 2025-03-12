from datetime import datetime

def calc_bmi(weight,height):
    bmi=weight/(height**2)
    return round(bmi,2)


def add_bmi(height,weight,bmi):
    date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    f=open("bmi.txt","a")
    
    f.write(f"{date}, Height: {height}m, Weight: {weight}kg, BMI: {bmi}\n")
    
    print("BMI recorded successfully")
    
    f.close()
    
height=float(input("Enter Height :"))
weight=float(input("Enter Weight :"))

bmi=calc_bmi(height,weight)
print("BMI is",bmi)

add_bmi(height,weight,bmi)