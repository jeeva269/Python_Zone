# Instance Method in Python

class student:
    name = "Jeeva"
    age = 21

    def printall(self,gender):
        print("Name : ",student.name)
        print("Age : ",student.age)
        print("Gender :", gender)

o = student()

"""
o.printall()
student.printall(o)
"""

# additional added

o.printall("Male")
student.printall(o,"Male")