# Main Menu of the Banking Application

# Create & Initialize variables
# print straight line
Straightline = "—" *40


# Main Menu
def MainMenu():

    # title
    print(Straightline)
    # ---------- Menu ----------
    print(f"Banking Application".center(40))
    print(Straightline)

    print(f"\n\t 1. Show Balance"
          f"\n\t 2. Deposit"
          f"\n\t 3. Withdraw"
          f"\n\t 4. Exit"
          )

    print(Straightline)
    # ---------- User Input ----------
    while True:
        try:
            choice = int(input("Enter your choice: "))
            # if choice out of range print an error message
            if choice not in [1, 2, 3, 4]:
                print("Please enter a Valid Choice. Please Try Again")
            # if choice in range return
            else:return choice
        except ValueError: print("Please enter a Valid Number")