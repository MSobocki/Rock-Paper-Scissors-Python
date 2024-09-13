import random

game_list = {1: "Paper", 2: "Rock", 3: "Scissors"}  # Creating [game_list] dictionary and populating it with items
keys = game_list.keys()  # assigning [keys] variable with keys from [game_list]
val = game_list.values()  # assigning [values] variable with vaules from [game_list]
victories = {1: 2, 2: 3, 3: 1}  # Win conditions


# Function returning a random number in range 1 to 3
def luck():
    return random.randint(1, 3)


# Creates a choosing list from dictionary [keys] and [val]ues using for loop
def game_chooser():
    print("Take your pick:")
    for k, v in game_list.items():
        print(f"{k} - {v}")


# Creating function that allows us to make automatic response
# it takes random number [randnum which has range 1-3] and we substract 1 from it to match list index range [0-2]
# Then we can use this to get response based on a list instead of writting it manualy with print() function
def description(desc):
    key_list = list(val)[desc - 1]
    variable_desc = print(f'I have chosen {key_list}')
    return variable_desc


# checking if user input is integer and in range
# then printing and calling appropriate functions
def user_input_check(x):
    if x in range(1, 4):
        print(f"You have chosen {list(val)[x - 1]}")
        choices(x)
    else:
        print("Wrong number! Try again!\n")
        game_chooser()
        x = int(input())
        user_input_check(x)


# Game Core
# We call luck() function which generates random number and assigning it to [randnum] variable
# Calling description function using randnum as an argument
# then create loop to go through k (keys) and v (values) in [victories] dictionary
# we nest an if conditions. If k(keys) is equal to user_input_val(int) and v(values) equals random number [randnum]
# when those conditions are met for loop checks are those vaules in items in victories dictionary
# e.q.: randnum = 2 and user_input_val = 1 there is no item 2:1 in our disctionary (victories = {1:2, 2:3, 3:1})
# elif we change that it's searching by randnum as key and user_input_val as Value
# basically we switch variable assignment resulting in reversing search.
# if any of those conditions are met we then print with (f)ormating element and new line (\n)
# + we convert val discitionary to list (top of the page [val = game_list.values()])
# we use k(key) - 1 as an index of the list (we use -1 because list indexing start at 0) same thing applies to v(values)
# Using Break to stop the loop and we call PlayAgain() for menu after the game results
def choices(usr_input_val):
    randnum = luck()
    description(randnum)
    for (k, v) in victories.items():
        if k == usr_input_val and v == randnum:
            print(f"\n{list(val)[k - 1]} beats {list(val)[v - 1]}\n")
            print("You Won!")
            break
        elif k == randnum and v == usr_input_val:
            print(f"\n{list(val)[k - 1]} beats {list(val)[v - 1]}\n")
            print(("I Won!"))
            break
        elif randnum == usr_input_val:
            print("\nIt's a Tie!")
            break
    PlayAgain()


# in this function we use error handling try: except: in while loop and ValueError - Forces user to put right number
# Asking user to put number 1 or 2 then converting it to integer
# if condition: if input is equal to 1 then call game_chooser function and ask new input with converting to integer
# elif: print msg and quit() to close the terminal
# when user puts anything else then integer it asks again until user puts right number 1 or 2
def PlayAgain():
    print(f"\nDo you want to play again?\n"
          f"1 - Yes\n"
          f"2 - No\n")
    usr = input()
    y = int(usr)
    if y == 1:
        game_chooser()
        x = int(input())
        user_input_check(x)
    elif y == 2:
        print("goodBye")
        quit()
    elif y != 1 or 2:
        print("Wrong input! Try Again!")
        PlayAgain()


# staring funcion getting user input converting it into integer and assigning it to variable x
# value of varriable x is then transfered into user_input_check function
# If user input has an error it will print a msg and run the function again
def start():
    while True:
        try:
            game_chooser()  # Calling function to show game list
            x = int(input())
            user_input_check(x)
            break
        except ValueError:
            print("Must be a number!")


start()  # calling function at the beginning
