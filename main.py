import json


f = open("bikes.json", "r") #reads from JSON bike file

content = f.read() #assigns the content of the file to a variable
if content:
    stock = json.loads(content) # converts content of json file to python list of dictionaries
else:
    stock = []

f.close()

def info_bike(bike):
    print('-'*50)
    print("Model:", bike['model'])
    print("price:", bike['price'])
    print("colour:", bike['colour'])
    print("size:", bike['size'])
    print("gender:", bike['gender'])
    print("quantity:", bike['quantity'])
    print('-'*50)


def menu():
    print("Press 1: To add stock. ")
    print("Press 2: To check stock. ")
    print("Press 3: To enter a customer purchase. ")
    print("Press q: To quit the program. ")
    return input("What would you like to do? ")


# DRY Don't repeat yourself!
while True:
    choice = menu()
    if choice == "1":
        print("Please enter this information:")
        model = input("Model: ")
        # result of input is string so I need cast it to the float
        price = float(input("Price in DKK: ")) #cast to float
        colour = input("Colour: ")
        size = input("Size in cm: ")
        gender = input("M for Mænd eller K for Kvinde: ")
        quantity = int(input("Quantity: "))  # cast to integer

        bike = {
            "model": model,
            "price": price,
            "colour": colour,
            "size": size,
            "gender": gender,
            "quantity": quantity
        }
        stock.append(bike)
        print("Successfully added new bike!")
        info_bike(bike)

    elif choice == "2":
        for item in stock:
            info_bike(item)

    elif choice == "3":
        import sales

    elif choice == "q":
        f = open("bikes.json", "w") #removes whole content of the file
        content = json.dumps(stock) # convert list to the json string
        f.write(content)
        f.close()
        break

    else:
        print("WRONG INPUT!!!")
print("The program has ended")
