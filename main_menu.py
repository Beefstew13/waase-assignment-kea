# This is the first menu the user will see when logging into the program
import sys

def main():
    login()

def login():
    username = "BikeShopOwner"
    password = "Hello1234"
    getusername = input("Please enter username")
    getpassword = input("Please enter password")
    if getusername == username and getpassword == password:
        print("Access Granted - Welcome to the Bikeshop System")
        main_menu()

def main_menu():
    print('-'*50)
    print()

    choice = input("""
Press 1 for Sales\n
Press 2 for Warehouse\n
Press Q to quit\n

Please enter your choice: """)
    if choice == "1":
        import sales
    elif choice == "2":
        import main
    elif choice == "Q" or choice == "q":
        sys.exit(0)
    else:
        print("You must only select either 1, 2 or Q.")
        print("Please try again")
        main_menu()

main()

"""

def main_menu(): # Creates the overall menu, where the user chooses which of the systems, warehouse and sales, the user wishes to go to.
    print('-'*50) # Prints 50 times - for user experience
    print('-'*50)
    print("Press 1 for Sales")
    print("Press 2 for Warehouse")
    print("Press any other tab to quit")
    print('-'*50) # Prints 50 times - for user experience
    return input() # Prints what the user chooses

main()

while True:
    choice = main_menu()
    if choice == "1":
        print("You chose 1")
        # import sales python file (the file name should not include the .py)

    elif choice == "2":
        print("You chose 2")
        import warehouse

    else:
        break
"""
