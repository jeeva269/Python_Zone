# Dictionaries and Its Function in Python

user = {
    "name": "Ram",
    "age": 25,
    "isMarriage": True
}

print(user)
print(type(user))
print(user['name'])
print(user.get('age'))
print(user.keys())
print(user.values())
print(user.items())

# For loop

for x in user:
    print(x,"",user[x])

for x in user.values():
    print(x)

for x in user.keys():
    print(x)

for x,y in user.items():
    print(x,y)        

# if Statement la check pannala

if "age" in user: 
    print("present")
      
# Changing values

user.update({"gender":"male"})
print(user)

user["age"]=30
print(user)

user.pop("age")
print(user)

# Dictionary kulla dictionary na Nested Dictionary

users={
    "user1": { 
        "name": "ram",
        "age": 25,
        "isMarried": True
    },
"user2": { 
        "name": "Sam",
        "age": 30,
        "isMarried": False
    }
}