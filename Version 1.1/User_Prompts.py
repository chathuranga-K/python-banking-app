# Exit Menu
# Asking a dialogue to confirm whether the user wants to quit the program or not

# Import Modules
import os
import io
import sys

# Set UTF-8 encoding for stdout
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Create & Initialize variables
# print straight line
Straightline = "—" *40

# prompt user to confirm termination of program
def ExitMenu():
    while True:
        try:
            print(Straightline) # print a straight line
            user_input = input("Do you want to exit? (YES/NO) ").strip().lower()

            # checks whether the user entered 'YES'
            if user_input in ['yes', 'y']:return True
            # checks whether the user entered 'NO'
            elif user_input in ['no', 'n']:return False

            # otherwise print Error
            else:print("Error! Please Enter the Correct Input (YES/NO)")
        # if the user input an invalid input, print error
        except ValueError:print("Please enter a valid input")
        else:print("Error Occurred! Please Try again")


# prompt user to enter an amount
def UserAmount():
    while True:
        try:
            print(Straightline) # print a straight line
            amount = float(input("Please enter the amount: "))
            return amount

        # if the user input an invalid input, print error
        except ValueError:print("Please enter a valid Amount")


# clear the terminal
def ClearTerminal():
    if os.name=='nt':
        os.system('cls') # for Windows systems
    else:
        os.system('clear') # for Mac/Linux systems
