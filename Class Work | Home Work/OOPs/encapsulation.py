class Bank:
    def __init__(self,account_number,holder,balance):
        self.account_number=account_number
        self.holder=holder
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited ${amount}. New Balance ${self.__balance}")
        else:
            print("You entered invalid amount")

    def withdraw(self,amount):
        if amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdrawn ${amount}. New Balance ${self.__balance}")
        else:
            print("you entered invalid amount")

    def view_balance(self):
        return f"Current Balance : ${self.__balance}"

account=Bank(650000,"Ashok",1000)

print(account.view_balance())

account.deposit(500)

account.withdraw(250)

print(account.view_balance())
