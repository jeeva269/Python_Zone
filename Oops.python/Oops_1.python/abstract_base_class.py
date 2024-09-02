# Abstract Base Class in python

from abc import ABC,abstractmethod

class Bank(ABC):
    
    @abstractmethod
    def loan(self):pass

    @abstractmethod
    def credit(self):pass

    @abstractmethod
    def debit(self):pass

class HDFC(Bank):

    def loan(self):
        print("We can provide 7.5% Interest loan")

    def credit(self):
        print("HDFC provide credit")

    def debit(self):
        print("HDFC provide debit")

o = HDFC()
o.loan()
o.credit()
o.debit()                   