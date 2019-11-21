# This is the first menu the user will see when logging into the program
import sys

def main():
    login()

def login():
    username = "BikeShopOwner"
    password = "Hello1234"
    getusername = input("""
--------------------------------------------------
Please enter username
--------------------------------------------------

""")
    getpassword = input("""
--------------------------------------------------
Please enter password
--------------------------------------------------

""")
    if getusername == username and getpassword == password:
        print()
        print('-'*50)
        print("Access Granted - Welcome to the Bikeshop System")
        print('-'*50)
        print()
        main_menu()

def main_menu():
    choice = input("""
--------------------------------------------------
Press 1 for Sales\n
Press 2 for Warehouse\n
Press Q to quit\n
--------------------------------------------------

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
