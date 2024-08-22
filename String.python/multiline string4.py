# Multiline string in one line...

a = """
This project aims to design and develop an e-kart 
platfrom that provides a seamless online shopping 
experience for customers.
"""
print(type(a))
print(a)

''' 
Getting Multiline input in python...
    join cories
'''

para=["25","22","33","55","75"]
print(','.join(para))

# program and .join...

para=[]
print("Enter a Para : ")

while True:
    line=input()
    if line:
        para.append(line)
    else:
        break
print(para)        
output='\n'.join(para)

print(output)







