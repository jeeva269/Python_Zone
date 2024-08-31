# try block in python

try:
    a = 10 / 0
except Exception as e:
    print(e)

# try except else in python

try:
    a = 10 / 25
except Exception as e:
    print(e)
else:
    print("A value : ",a)        

# try finally except else in python

try:
    a = 10 / 0
except Exception as e:
    print(e)
else:
    print("A value : ",a)   
finally:
    print("Thank you")
