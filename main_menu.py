#thi is the first menu the user will see when logging into the program
 
  def menu(): # Creates the overall menu, where the user chooses which of the systems, warehouse and sales, the user wishes to go to.
    print('-'*50)
    print("Press 1 for Sales")
    print("Press 2 for Warehouse")
    print("Press any other tab to quit")
    print('-'*50)
    return input()

while True:
    choice = menu()
    if choice == "1":
        print("You chose 1")
        # import sales python file (the file name should not include the .py)

    elif choice == "2":
        import main

    else:
        break
