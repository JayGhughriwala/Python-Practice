#  First Of all create a time function for that it return a current time value

def getTime():
    import datetime
    return datetime.datetime.now()


print("This is a Health Management System")

#  Now for entry in the files or the retrive file from the datebase

#  1 for log entry
#  2 for retrive data

# val_choice  variable for the choice of the what to do by user for the system


val_choice = int(input("Enter 1 for log entry \nEnter 2 for retrive data \n \t\tEnter your choice :- "))

#  Now for press 1 for exercise
# 2 for food

#  val_ex_food  for the choice of the exercise or food

val_ex_food = int(input("Enter 1 for exercise \nEnter 2 for food \n\t\tEnter your choice :- "))

#  Now for the for which  user you want to log the exercise or food

#  here are only three users Jay, John, Jack

#  val_user_choice for the choice of the user

val_user_choice = int(input("Enter 1 for Jay \nEnter 2 for John \nEnter 3 for Jack \n\t\tEnter your choice :- "))

#  Now for the log entry

if val_choice == 1:
    if val_ex_food == 1 and val_user_choice == 1:
        with open("healthSystemContent/Jayfood.txt", "a") as f:
            exercise_name = input("Enter the exercise :- ")
            f.write(str(getTime()) + " : " + "Exercise " + exercise_name+" \n")
            print("Exercise logged successfully")
    elif val_ex_food == 1 and val_user_choice == 2:
        with open("healthSystemContent/Johnfood.txt", "a") as f:
            exercise_name = input("Enter the exercise :- ")
            f.write(str(getTime()) + " : " + "Exercise " + exercise_name+" \n")
            print("Exercise logged successfully")
    elif val_ex_food == 1 and val_user_choice == 3:
        with open("healthSystemContent/Jackfood.txt", "a") as f:
            exercise_name = input("Enter the exercise :- ")
            f.write(str(getTime()) + " : " + "Exercise " + exercise_name+" \n")
            print("Exercise logged successfully")
    elif val_ex_food == 2 and val_user_choice == 1:
        with open("healthSystemContent/Jayfood.txt", "a") as f:
            food_name = input("Enter the food :- ")
            f.write(str(getTime()) + " : " + "Food " + food_name+" \n")
            print("Food logged successfully")
    elif val_ex_food == 2 and val_user_choice == 2:
        with open("healthSystemContent/Johnfood.txt", "a") as f:
            food_name = input("Enter the food :- ")
            f.write(str(getTime()) + " : " + "Food " + food_name+" \n")
            print("Food logged successfully")
    elif val_ex_food == 2 and val_user_choice == 3:
        with open("healthSystemContent/Jackfood.txt", "a") as f:
            food_name = input("Enter the food :- ")
            f.write(str(getTime()) + " : " + "Food " + food_name+" \n")
            print("Food logged successfully")
elif val_choice == 2:
    if val_ex_food == 1 and val_user_choice == 1:
        with open("healthSystemContent/Jayfood.txt", "r") as f:
            print(f.read())
    elif val_ex_food == 1 and val_user_choice == 2:
        with open("healthSystemContent/Johnfood.txt", "r") as f:
            print(f.read())
    elif val_ex_food == 1 and val_user_choice == 3:
        with open("healthSystemContent/Jackfood.txt", "r") as f:
            print(f.read())
    elif val_ex_food == 2 and val_user_choice == 1:
        with open("healthSystemContent/Jayfood.txt", "r") as f:
            print(f.read())
    elif val_ex_food == 2 and val_user_choice == 2:
        with open("healthSystemContent/Johnfood.txt", "r") as f:
            print(f.read())
    elif val_ex_food == 2 and val_user_choice == 3:
        with open("healthSystemContent/Jackfood.txt", "r") as f:
            print(f.read())



