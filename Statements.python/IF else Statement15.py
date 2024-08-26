# if else Statements...

'''
Write a program check vote eligibility by enter hir/heer name and age
'''
name = input("Enter a Name : ")
age = int(input("Enter a age : "))
if age>=18:
    print(name,"age is", age, "Eligible for vote." )
else:
    print(name,"age is", age, "Not Eligible for vote." )    