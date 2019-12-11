from ui import UserInterface


def main():  # When main is called, it calls the login funciton
    login()


def login():  # To enter the main_menu the input has to be the same as Username and Password
    username = "admin"
    password = "admin"
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
    else:
        print("Username or password is incorrect. Try again! ")
        login()  # Runs the login function until correct username and password is typed


def main_menu():
    ui = UserInterface()

    while True:
        choice = input("""
    --------------------------------------------------
    Press 1 To Add New Stock\n
    Press 2 To Check the Current Stock\n
    Press 3 To Add Item to Cart\n
    Press 4 To Make a Purchase\n
    Press 5 To Display a Cart\n
    Press 6 To Empty a Cart\n
    Press 7 To Display all Reports\n
    Press Q to quit\n
    --------------------------------------------------

    Please enter your choice: """)
        if choice == "1":
            model = input("Please enter model")
            price = input("Please enter price")
            colour = input("Please enter colour")
            size = input("Please enter size")
            gender = input("Please enter gender")
            quantity = input("Please enter quantity")
            ui.add_new_bike(model, price, colour, size, gender,
                            quantity)  # sends arguments to the method
            print("Successfully added to stock!")
        elif choice == "2":
            ui.display_stock()
        elif choice == "3":
            ui.add_to_cart()
        elif choice == '4':
            ui.make_purchase()
        elif choice == '5':
            ui.display_cart()
        elif choice == '6':
            ui.empty_the_cart()
        elif choice == '7':
            ui.display_reports()
        elif choice == "Q" or choice == "q":
            break
        else:
            print("You must only select either 1, 2 or Q.")
            print("Please try again")


# This is the first menu the user will see when logging into the program
main()
