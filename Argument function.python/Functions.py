# Recursive Function in python

def factorial(x):
    if x == 1:
        return 1
    else:
        return(x*factorial(x-1))
print("Factorial :",factorial(5))

# Lambda Function in python

'single arugument'

c = lambda a: a + 50 
print(c(5))

'Mulitipul arugument'

c = lambda a,b:a*b
print(c(10, 25))

