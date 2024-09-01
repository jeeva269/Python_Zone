# Instance Attributes in Python

class user:
    course = 'Java'

o = user() # new object created
print(user.__dict__) 
print(user.course)   

# instance check 

print(o.__dict__)
print(o.course)

o.course = 'Python'
print(o.__dict__)
print(o.course)

# new object created agian

o1 = user()
print(o1.course)
