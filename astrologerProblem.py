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
inp =input("input 1 for pattern as it is or input 0 for pattern reverse --> ?")
if inp == 1:
    for i in range(n):
        for j in range(i+1):
            print(" * ",end="")
    print(" ")
#
#   in else pattern like this

#  * * * * *
#  * * * *
#  * * *
#  * *
#  *
else:
    for i in range(n,0,-1):
        for j in range(0,i):
            print(" * ",end="")
        print("")