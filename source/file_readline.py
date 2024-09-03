try:
    file=open("jeeva.txt","r")
    print(file.readline())
    print(file.readline(4)) # charater view

    print(file.readlines()) # overall lines read

except FileNotFoundError:    
    print("Error : File Not found")
else:
    file.close()