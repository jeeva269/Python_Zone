# Class Method Decorator in python

class student:

    count = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        student.count += 1 

    def printDetail(self):
        print("Name : ",self.name,"Age : ",self.age)

    @classmethod
    def total(cls):
        return cls.count

o = student("Joes", 24)
o.printDetail()

print("Total admission : ", o.total())

a = student("Raja", 23)
a.printDetail()

print("Total admission : ", student.total())

print("Total admission : ", o.total())
