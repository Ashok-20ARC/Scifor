from operations import *

def perform_calculation():
    print("Select operation:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    
    choice=int(input("Enter choice (1/2/3/4): "))
    if choice not in [1,2,3,4]:
        print("Invalid choice. Please select a valid operation.")
        return
    
    num1=float(input("Enter first number : "))
    num2=float(input("Enter second number : "))
    
    if choice==1:
        print(f'Result: {add(num1,num2)}')
    elif choice==2:
        print(f'Result: {sub(num1,num2)}')
    elif choice==3:
        print(f'Result: {mul(num1,num2)}')
    elif choice==4:
        print(f'Result: {div(num1,num2)}')