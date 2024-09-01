# Static Method in python

class student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printDetail(self):
        print("Name : ",self.name,"Age : ",self.age)

    @staticmethod
    def Welcome():
        print("Welcome to our Institution")

s1 = student("Raja", 25)
s1.printDetail()
s1.Welcome()

s2 = student("Joes", 20)
s2.printDetail()
s2.Welcome()
