# Overwrite a File in python

try:
    file=open("jeeva.txt","w") #overwrite
    file.write("Dream Big")
    file.close()

    file=open("jeeva.txt","r")
    for line in file:
        print(line)

except FileNotFoundError:    
    print("Error : File Not found")
else:
    file.close()
