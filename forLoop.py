# list1 = [[1,"One"],[2,"Two"],3,4,5,6,7,8]

# for i,word in list1:
#     print(i,word)

# quiz for see it's number or not

list1 = ["Jay", "jay", 1, 2, 3, 50, 163, 96]

for item in list1:
    if str(item).isnumeric() and item >= 6:
        print(item, "is a number and greater than 6")
