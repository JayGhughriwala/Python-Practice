print("This is a Faulty calculator for the below calculation")
print("For this calculation it return a wrong answer \n\t 45 * 3 = 555\n\t 56 + 9 = 77\n\t 56 / 6 = 4")

num1 = int(input("Enter the first number : - "))
num2 = int(input("Enter the second number :- "))

op = input("Enter the character for the operation :- ")

if op == "+":
    if num1 == 56 and num2 == 9:
        print("The answer is 77")
    else:
        print("The answer is ", num1 + num2)
elif op == "*":
    if num1 == 45 and num2 == 3:
        print("The answer is 555")
    else:
        print("The answer is ", num1 * num2)
elif op == "/":
    if num1 == 56 and num2 == 6:
        print("The answer is 4")
    else:
        print("The answer is ", num1 / num2)
elif op == "-":
    print("The answer is ", num1 - num2)
else:
    print("Invalid operation")