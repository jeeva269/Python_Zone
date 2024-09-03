# Delete a File in python

import os

if os.path.exists("txt1.txt"):
    os.remove("txt1.txt")
    print("Deleted Successfully")
else:
    print("File not Found")



