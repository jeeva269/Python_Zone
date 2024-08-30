# List and Its Function in Python...
'''
Sequence type
Mutable 

#list na oru type...

a[5]
a={1,2,3,4,5}
a{0}
'''
a=[1,2,3,4,5]
print(a)
print(type(a))
a[0]=100
print(a)
print("---Slicing---")
print(a[1])
print(a[-1])
print(a[0:3])
print(a[2:])
print(a[:3])

print("---------------------")
 #Mulitiple data type in Single list la store pannala

a=[1,True,'ram',2.5]
print(a)
print(type(a))
print(a[0]," type is ",type(a[0]))
print(a[1]," type is ",type(a[1]))
print(a[2]," type is ",type(a[2]))
print(a[3]," type is ",type(a[3]))

print("---------------------")
 #Nested list store pannala

a=[1,True,'ram',2.5,[1,2,3,4]]
print(a)
print(type(a))
print(a[4]," type is ",type(a[4]))
print(a[4][1])

print("---------------------")
 #list la iruka In-bulit funtion

a=[10,25,35,45]
print(a)
a.clear()
print(a)

a=[10,25,35,45]
b=a.copy()
print(b)

a=[10,25,35,45,25,60,25]
print(a.count(25))

a=[10,25,35,45,25,60]
print(a.index(25))

a=[10,25,35,45,55,76,88]
print(len(a))

a=[10,25,35,45,55,76,88]
print(max(a))

a=[10,25,35,45,55,76,88]
print(min(a))

a=[10,25,35,45,55]
print(a)
a.pop(0) #remove element using index
print(a)

a=[10,25,35,45,25,60,25]
a.remove(25) #values vachi remove pannunum
print(a) 

print("-------------------")

names=["Ram"]
print(names)
names.append("Sam")
names.append("Ravi")
names.append("Kumar")
print(names)
names2=["Sara","Zara"]
names.extend(names2)
print(names)
names.insert(0,"suriya")
print(names)
