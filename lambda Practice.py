
print("This is the program of the pratice of the lambda function")
def add(a,b):
    return a+b
#  Now here for the addition of two numbers I created a simple funciton
print("Enter the two numbers -->> ")

a = int(input("Enter the first number :- "))
b = int(input("Enter the second number :- "))
addd = lambda  a,b: a+b
print("The addition of the two numbers using function ", add(a,b))
print("The addtion of the two numbers using a lambda function ", addd(a,b))


#  Now it will be done by the lamba function



