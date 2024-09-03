# Open a File in Python

file_path = r"/home/manjula/Desktop/python/source/jeeva.txt" # Using raw string for Windows file path

with open(file_path, 'r') as file:  # 'with' statement ensures the file is properly closed
    print(file.read())


# simple command

"""
file = open("jeeva.txt","r")
print(file.read())

"""

# Error command

"""
try: 
    file=open("home/manjula/Desktop/python/source/testt1.txt","r") #read file
    print(file.read())
except FileNotFoundError:    
    print("Error : File Not found")
else:
    file.close()
"""

