# No Return Type Without Argument Function in Python

'a,b la input kuduthu c la print pannikala'

def add():
    a = int(input("Enter The Value of A : "))
    b = int(input("Enter The Value of B : "))
    c = a + b
    print(c)

add()

# No Return Type With Argument Function in Python

'direct ah a,b assign pannirala,apram kila sub la value kuduthukala'

def sub(a,b):
    c = a - b
    print("Difference : ",c)

sub(25,2)    

# Return Type Without Argument Function in Python

'''a,b la int vagi input kuduthutu,c la print 
panni thiruba c ah return panni x la print pandrom'''

def mul():
    a = int(input("Enter The Value of A : "))
    b = int(input("Enter The Value of B : "))
    c = a * b
    return c
 
x = mul()
print("Mul",x)   

# Return Type With Argument Function in Python

'value direct ah assign pannitu,retrun panni X la print pandrom value vae'

def div(a,b):
    c = a / b
    return c

x = div(25,2)
print("Division",x) 

# Arbitrary Arguments Function in Python(*) 

'Neriya arguments neega assign pannikala Arbitrary la'

def class_10(*students):
    print(students)

class_10("Ram","Sam","Raja","Sara","Kumar")

#  Keyword Arguments Function in Python

'''change panni kuduthalum python crt aduthukum
two keyword tha kudu mudiyum'''       

def message(name, age):
    print(name," age is ", 24)

message(age=24, name="Ram")

# Arbitrary Keyword Arguments in Python (**)

'but ethu la neriya keywords kuduthukala ** use panni'

def bioData(**data):
    print(data)

bioData(name="Ram Kumar",age=24,gender="Male")    

#  Default Parameter Function in Python

'default ahh oru value function la kuduthurom'

def user(name, city="Salem"):
    print(name," is from ", city)

user("Ram", "Namakkal")
user("Sam")    

# Passing a List as an Argument in Function Python

'list value funtion la direct ah pass panna mudiyum'

def total(marks):
    return sum(marks)
print("Total:",total ([55,67,87,67,88]))
    