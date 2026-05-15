# Banking Application
# Version 1.0

# import packages
import Constants # Constant Variables
import User_Prompts

from Main_Menu import MainMenu # Main Menu
from User_Prompts import UserAmount, ClearTerminal  # User Amount

# Create & Initialize variables
# print straight line
Straightline = "—" *40


while True:
    # run main menu
    choice = MainMenu()

    # ---- Show Balance ----
    if choice == 1:
        # print available balance
        print(Constants.CurrentBalance)

    # ---- Deposit ----
    elif choice == 2:
        askAmount = UserAmount() # initialize variables
        # add Deposit amount to Current Balance
        Constants.CurrentBalance += askAmount
        print("Deposit SUCCESSFUL")
        print(f"\n\tYour Balance is {Constants.CurrentBalance}") # print balance amount

    # ---- Withdraw ----
    elif choice == 3:
        # initialize variables
        askAmount = UserAmount() # Withdraw Amount
        WithdrawLimit = Constants.WithdrawLimit # Withdraw Limit

        # check whether the Withdrawal amount is exceeding the Current balance
        if askAmount <= Constants.CurrentBalance:
            # check whether the Withdrawal Limit is exceeding or not
            if WithdrawLimit <= Constants.CurrentBalance-askAmount:

                # subtract Withdrawal amount from Current Balance
                Constants.CurrentBalance -= askAmount
                print("Withdraw SUCCESSFUL")
                print(f"\n\tYour Balance is {Constants.CurrentBalance}") # print balance amount

            # Withdrawal amount is exceeding the Limit
            else: print("Withdraw FAILED")
        # account balance is exceeding the withdrawal amount
        else: print("Sorry your current balance is not sufficient")

    # ---- Exit ----
    elif choice == 4:break # Program terminates

    # if any other common error occurred print an error message
    else:print("Error Occurred. Please Try Again")

    if User_Prompts.ExitMenu(): break # prompt user to confirm exit
    User_Prompts.ClearTerminal() # clear the Terminal before continue
