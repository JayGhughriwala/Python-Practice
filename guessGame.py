print("This is the number guessing game ")
print("In this game number is already generated and you have to guess the number")
print("You have to guess the number between 1 to 100 ")
print("You have to guess the number in less than 10 attempts")

# generate a random number between 1 to 100
import random
number = random.randint(1, 100)

#  Now Asking the user to guess the number

attempts = 10
while (attempts > 0):
    guess = int(input("Enter the number :- "))
    if guess > 100:
        print("Your entered number is greater than 100 ")
    elif guess < 1:
        print("Your entered number is less than 1")
    elif guess == number:
        print("You have passed the game in ", attempts, " attempts")
        break
    elif 1 <= number <= 10:
        if 1 <= number <= 5:
            print("Yes Number is between 1 to 5")
        elif 6 <= number <= 10:
            print("Yes Number is between 6 to 10")
    elif 11 <= number <= 20:
        if 11 <= number <= 15:
            print("Yes Number is between 11 to 15")
        elif 16 <= number <= 20:
            print("Yes Number is between 16 to 20")
    elif 21 <= number <= 30:
        if 21 <= number <= 25:
            print("Yes Number is between 21 to 25")
        elif 26 <= number <= 30:
            print("Yes Number is between 26 to 30")
    elif 31 <= number <= 40:
        if 31 <= number <= 35:
            print("Yes Number is between 31 to 35")
        elif 36 <= number <= 40:
            print("Yes Number is between 36 to 40")
    elif 41 <= number <= 50:
        if 41 <= number <= 45:
            print("Yes Number is between 41 to 45")
        elif 46 <= number <= 50:
            print("Yes Number is between 46 to 50")
    elif 51 <= number <= 60:
        if 51 <= number <= 55:
            print("Yes Number is between 51 to 55")
        elif 56 <= number <= 60:
            print("Yes Number is between 56 to 60")
    elif 61 <= number <= 70:
        if 61 <= number <= 65:
            print("Yes Number is between 61 to 65")
        elif 66 <= number <= 70:
            print("Yes Number is between 66 to 70")
    elif 71 <= number <= 80:
        if 71 <= number <= 75:
            print("Yes Number is between 71 to 75")
        elif 76 <= number <= 80:
            print("Yes Number is between 76 to 80")
    elif 81 <= number <= 90:
        if 81 <= number <= 85:
            print("Yes Number is between 81 to 85")
        elif 86 <= number <= 90:
            print("Yes Number is between 86 to 90")
    elif 91 <= number <= 100:
        if 91 <= number <= 95:
            print("Yes Number is between 91 to 95")
        elif 96 <= number <= 100:
            print("Yes Number is between 96 to 100")
    else:
        print("You have entered wrong number")
    attempts -= 1
    if attempts == 0:
        print("You are failed to guess the number")
        break
    else:
        print("You have", attempts, "attempts left")
        continue
print("The number is", number)
