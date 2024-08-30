# Sets and Its Function in Python..

names={'Ram','Sam','Ravi'}
print(names)
print(type(names))

# Access Values Using For loop

for name in names:
    print(name)

# Adding New element

names.add('sara')
print(names) 

# Update another Set of data

a= {'kumae','sundar','suresh'}
names.update(a)
print(names)

# Remove funtion

names.remove('kumae')
print(names)

names.discard('jeeva') #irutha remove pannum ilana appdiyae viturum
print(names)

names.pop() #random value remove at last
print(names)

names.clear() #value ellame clear pannirum
print(names)

'''del names''' #overall atha set ellame delete pannirum

names={'Ram','Sam','Ram','Ravi','kumae','sundar','suresh'}
print(names)

# Union funtion

a = {1,2,3,4}
b = {'a','b','c','d'}
c =a.union(b)
print(c)
a.update(b)
print(a)

# Intersection 
'comman ahh iruka value'

a ={1,2,3,4,5}
b ={5,6,7,8,9}

c=a.intersection(b)
print(c)
a.intersection_update(b)
print(a)


# symmetric_diffierence
'different ahh iruka value'

a ={1,2,3,4,5}
b ={1,2,7,8,9}

c=a.symmetric_difference(b)
print(c)
a.symmetric_difference_update(b)
print(a)

# isdisjoint (is munnadi na Boolean)
'true or false '

a = {5,6,7}
b = {5,6,7,8}
c =a.isdisjoint(b) # value different ah irutha true ila na false
print(c)

c =a.issubset(b) # value same ah irutha true ila na false
print(c)

c=a.issuperset(b) # a la iruka value ellame b la irutha true ila na false
print(c)
