# Operator Overloading in python
"""
a = 10
b = 20
print(a+b) =>30

a = "jee"
b = "va"
print(a+b) =>jeeva(sting) =(Con catenater)
"""
class addition:
    
    def __init__(self,a):
        self.a = a

    def __add__(o1,o2):
        return o1.a + o2.a
    
    def __sub__(o1,o2):
        return o1.a - o2.a
    
o1 = addition(10)
o2 = addition(20)

print("Total : ", (o1+o2))
print("Difference : ", (o1 - o2))