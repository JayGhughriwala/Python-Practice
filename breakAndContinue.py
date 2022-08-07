print("This is the practice of the break and continue statement")
i=1
while(True):
    inp=int(input("Enter the number :- "))
    if inp >100:
        print("Your entered number is greater than 100 hence breaking the loop")
        break
    else:
        print("Your entered number is less than 100 hence continuing the loop")
        continue
