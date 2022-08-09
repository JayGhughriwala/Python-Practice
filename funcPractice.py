print("This is the practice of the function practice")


# print(sum((5,6)))  because it is a tupple it is a tupple so we required to put a two parenthesess

#  Now create a our own function

# def func1():
#     print("This is a function")
#
#
# func1()

# def func2(num1,num2):
#     print("The sum of the two numbers is ", num1 + num2)
#     print("The difference of the two numbers is ", num1 - num2)
#
# func2(4,2)

#  Now create a function that return a value

# def func(num1,num2):
#     #  This function return a average of the two numbers
#     return int((num1 + num2) / 2)
#
# print("now Asking a two numbers first")
#
# num1 = int(input("Enter the first number :- "))
# num2 = int(input("Enter the second number :- "))
#
# print("The average of the two numbers is ", func(num1,num2))

#  Now practice of the docstrings

def func(num1,num2):
    """
    This function return a average of two numbers only strictly
    :param num1:
    :param num2:
    :return:

    """
    return int((num1 + num2) / 2)

#  Now in the main function we wil call the function
#
# print("Now asking the user to enter a two number ")
# a = int(input("Enter the first number :- "))
# b = int(input("Enter the second number :- "))
#
# print("The average of the two numbers is ", func(a,b))
# # Now printing the docstring

print(func.__doc__)