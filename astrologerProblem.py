# this is a pattern problem for the astrologer

print("The program is starting ")
print("Please enter your name :- ")
name = input()
n = int(input("Please enter the \"n\" value for the pattern :- "))
print("Hello " + name + " , the program is starting ")

# *
# **
# ***
# ****
# Pattern like this

for i in range(n):
    for j in range(i+1):
        print(" * ",end="")

    print(" ")