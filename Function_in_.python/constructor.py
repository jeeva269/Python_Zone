# list type Constructor..

print(list(range(5)))
print(list("Tutor joes"))

a=[10,50,100,25,85]
print(a)
a.sort()
print(a)

a=[10,50,100,25,85]
print(a)
a.sort(reverse=True)
print(a)

a=["Orange","Apple","Zebra"]
a.sort()
print(a)
a.sort(reverse=True)
print(a)

a=["Orange","Apple","Zebra"]
a.sort(key=len)
print(a)