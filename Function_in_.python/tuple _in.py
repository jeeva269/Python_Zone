# Tuples and Its Function in Python...

'''
Tuple
Immutable
Surrounded by round Brackets ()
'''

a = (1,2.4,True, "Ram")
print(a)
print(type(a))
print(a[1])
print(a[-1])
print(a[0:2])

b=list(a)
print(b)
b.append("Raja")
print(b)
print(type(b))

a =tuple(b)
print(b)
print(type(a))

# for loop ah vachi kuda pakala

for i in a:
    print(i)

if "Raja" in a:
    print("Raja is Found")
else:
    print("Not Found") 
          
print(len(a))

# Single item use panna you must put "," there:

a=(1,)
print(type(a))
'''del a'''
print(a)

# Easy ah Concatenate pannala

a=(1,2,3,4,5)
b=(6,7,8,)
c=a+b
print(c)
print(c.count(7))

# Nested typle

a =(1,2,3,4,5)
b =(6,7,8,9)
c =(a,b)
print(c)

# Duplicate data 

x =("jeeva",)*5
print(x)