print("This is the practice of recursion")
print(" First is the factorial of a number")

def factorialUsingIterative(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def factorialUsingRecursion(n):
    if n == 1:
        return 1
    else:
        return n * factorialUsingIterative(n-1)

print("The first is the factorial finding program -->> ")
n = int(input("Enter the number :- "))
print(" The factorial of the number using recursion is ", factorialUsingRecursion(n))
print(" The factorial of the number using iterative is ", factorialUsingIterative(n))

#  Now for the fibonacci series

def fibUsingRecursion(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibUsingRecursion(n-1) + fibUsingRecursion(n-2)

def fibUsingIterative(n):
    a = 1
    b = 1
    for i in range(3,n+1):
        c = a+b
        a=b
        b=c
        return c


print("Now Asking from the user for the fibonacci series")

n = int(input("Enter the number for finding the fibonaccci series :- "))

print("The fibonacci series of the number using recursion", fibUsingRecursion(n))

print("The fibonacci series of the number using iterative ", fibUsingIterative(n))

