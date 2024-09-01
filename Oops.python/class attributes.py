# Class Attributes in Python

class student():
    name = "Abitha"
    age = 20

# getattr method 

print(getattr(student, 'name'))
print(getattr(student, 'age'))
print(getattr(student,' gender','No such attribute found'))

# Dot . notation

print(student.name)
print(student.age)

# setattr

setattr(student, 'name', 'Jeeva')
print(student.name)

setattr(student, 'gender', 'Male')
print(student.gender)

# set city

student.city = 'Salem'
print(student.city)

# maping format like dici

print(student.__dict__)

# delete

delattr(student,"city")
print(student.__dict__)

del student.gender
print(student.__dict__)