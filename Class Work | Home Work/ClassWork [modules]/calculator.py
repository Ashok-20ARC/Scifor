from calculation import perform_calculation

print("----- Calculator ------")

while True:
    perform_calculation()
    another=input("Do you want to perform another calculation? (yes/no):").strip().lower()
    
    if another!='yes':
        print("Thank you for using the calculator. Goodbye!")
        break