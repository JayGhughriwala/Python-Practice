print("This is a Snake Water Gun game")
print("The Rule is simple mention below ")
print("\t 1. Snake will win if opponent choose Water")
print("\t 2. Water will win if opponent choose Gun ")
print("\t 3. Gun will win if opponent choose Snake")

print("Now Starting a game\n\n\n")
print("In this game you have 10 chances to guess the opponent's choice \n\t\"If you input a invalid choice your chances will be decreased and it will may down your chances of Winning")

print("After the 10 chances finished the result will be displayed")
print("\n\n\n")

user_Score = 0
computer_Score = 0
#  Now Start the game
import random

chances = 10
while chances > 0:
    print("Press \"1\" for Snake")
    print("Press \"2\" for Water")
    print("Press \"3\" for Gun")
    print("Enter Your choice :-  ", end="")
    choice = int(input())
    if choice > 3 or choice < 1:
        print("Invalid Choice Please enter your choice again")
        continue

    opponent_choice = random.randint(1, 3)
    if choice == 1:
        if opponent_choice == 2:
            print("You win Bcz opponent choose Water")
            user_Score += 1
        elif opponent_choice == 3:
            print("You lose Bcz opponent choose Gun")
            computer_Score += 1
        else:
            print("Draw Bcz  Both of you choose Snake ")
    elif choice == 2:
        if opponent_choice == 3:
            print("You win Bcz  opponent choose Gun")
            user_Score += 1
        elif opponent_choice == 1:
            print("You lose Bcz oppoment choose Snake")
            computer_Score += 1
        else:
            print("Draw Bcz Both of you choose Water")
    elif choice == 3:
        if opponent_choice == 1:
            print("You Win Bcz opponent choose Snake ")
            user_Score += 1
        elif opponent_choice == 2:
            print("You lose Bcz opponent choose Water")
            computer_Score += 1
        else:
            print("Draw Bcz Both of you choose Gun")
    chances -= 1



print("\n\n\n")
print("Your Score is ", user_Score)
print("Computer Score is ", computer_Score)
if user_Score > computer_Score:
    print("You Win")
elif user_Score < computer_Score:
    print("You Lose")
else:
    print("Draw")
print("\n\n\n")

