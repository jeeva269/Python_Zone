# Multiple Inheritance in Python

# (A and B two base class ) =(c one derived class)

class Father:
    def fishing(self):
        print("Fishing in Rivers")
    
    def chess(self):
        print("Playing chess from Father")

class Mother:
    def cooking(self):
        print("Cooking Food")
    
    def chess(self):
        print("Playing chess from Mother")   

class son(Mother,Father):
    def ride(self):
        print("Riding bicycle")

o = son()
o.ride()
o.fishing()
o.cooking()
o.chess()                         