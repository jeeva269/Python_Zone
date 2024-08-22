# string and string funtion...

s = "jeevanantham"
print(s)
print(type(s))
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.count("a"))
print(s.endswith("am"))
print(s.find("e"))
print(s.find("n", 6))
print(s.replace("j", 'J'))
a = "jeeva1234"
print("Is Upper : ", a.isupper())
print("Is Lower : ", a.islower())
print("Is Alpha Numeric : ", a.isalnum())
print("Is Alpha : ", a.isalpha())
s ="he\nis\ngood"
print(s)
print(s.splitlines())
print(s.splitlines(True))
a = "Jeeva is IT Junior Employee"
print(a.split(" "))
a = "Jeeva,is,IT,Junior,Employee"
print(a.split(","))
s = "      jeeva    "
print(len(s))
print(len(s.strip()))
print(len(s.lstrip()))
print(len(s.rstrip()))
s = '12-08-2024'
print(s.partition('-'))



