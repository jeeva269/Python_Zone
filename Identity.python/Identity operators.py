# Identity operators in python

'''
is 
is not 
'''
a = [1,2]
b = [1,2]
c = a
print(c)
print(id(a))
print(id(b))
print(id(c))

print(a is c)
print(a is b)

print(a==b)

print(a is not c)
print(a is not b)
print(a!=b)