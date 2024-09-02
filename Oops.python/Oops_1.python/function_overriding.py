# Function Overriding in python

class Employee:
    
    def workingHrs(self):
        self.hrs = 50

    def printHrs(self):
        print("Total working Hrs : ", self.hrs) 

class Trainee(Employee):
    
    def workingHrs(self):
        self.hrs = 60
 
    def resetHrs(self):
        super().workingHrs()

employee = Employee()
employee.workingHrs()
employee.printHrs()

trainee = Trainee()
trainee.workingHrs()
trainee.printHrs()

# Reset Trainee Hrs

trainee.resetHrs()
trainee.printHrs()