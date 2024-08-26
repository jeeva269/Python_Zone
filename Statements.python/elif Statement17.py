# elif statements...
'''
0 days     no fine
1 - 5      10 rupess fine
5 - 10     30 rupess fine
10 - 30    50 rupess fine
above 30   Membership cancel
'''
days = int(input("Enter the Days : "))  
if days == 0:
    print("Good no fine")
elif days >= 1 and days <= 5:
    print("Fine amount : ",days * 10)
elif days >5 and days <= 10:
    print("Fine amount : ",days * 30)    
elif days >10 and days <= 30:
    print("Fine amount : ",days * 50) 
else:
    print("Membership Cancel")       