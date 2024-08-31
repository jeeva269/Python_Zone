# Type of Exceptions in Python

print(dir(locals()['__builtins__']))

print(len(dir(locals()['__builtins__'])))

# Name error exception

try:
    print(a)
except NameError or e :
    print("A is  not Define")   

# value error exception

try:
    a = [10,20,30,40]
    print(a[10])
except IndexError as e:
    print("Invaild Index")        

# file open and read exception
    
try:
    f = open("test.txt")
except FileNotFoundError:
    print("File Not Found")
else:
    print(f.read())            