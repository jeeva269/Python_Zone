# Class Method in Python

class student:
    name = "Jeeva"
    age = 21

    def printall():
        print("Name : ",student.name)
        print("Name : ",student.age)

student.printall()    
print(student.__dict__)

# getattr

print(getattr(student,"printall"))
getattr(student,"printall")()

# dicti format call pannala

student.__dict__['printall']() #regular using in python