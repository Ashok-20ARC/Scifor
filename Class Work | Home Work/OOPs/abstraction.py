from abc import ABC, abstractmethod

class Bank(ABC):
    @abstractmethod
    def loan(self): pass

    @abstractmethod
    def credit(self): pass

    @abstractmethod
    def debit(self): pass

class HDFC(Bank):
    def loan(self):
        print("we can provide 7.5% interest loan")
        
    def credit(self):
        print("HDFC provide credit")
        
    def debit(self):
        print("HDFC provide debit")

    def card(self):
        print("Provide card")

o=HDFC()
o.loan()
o.credit()
o.debit()
o.card()
