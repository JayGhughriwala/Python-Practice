print("This is the practice of the try and except handling")
num1 = input("Enter the first number :- ")

num2 = input("Enter the second number :- ")

try:
    print(" The sum of two number is ", int(num1 + num2))
except Exception as e:
    print(e)
