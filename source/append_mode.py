# Append Mode File in python

try:
    file=open("jeeva.txt","a") #append
    file.write("Hi I am Jeeva")
    file.close()
    
    file=open("jeeva.txt","r")
    print(file.read())

except FileNotFoundError:    
    print("Error : File Not found")
else:
    file.close()
