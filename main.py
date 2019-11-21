import json


f = open("bikes.json", "r")

content = f.read() 
if content:
    stock = json.loads(content) # converts content of json file to python list of dictionaries
else:
    stock = []

f.close()

def info_bike(bike):
    print('-'*50)
    print("Model:", bike['model'])
    print("price:", bike['price'])
    print("description:", bike['description'])
    print("count:", bike['count'])
    print('-'*50)


def menu():
    print("Press 1: To add stock. ")
    print("Press 2: To check stock. ")
    print("Press 3: To enter purchase. ")
    print("Press q: To quit the program. ")
    return input("What would you like to do?")


# DRY Don't repeat yourself!
while True:
    choice = menu()
    if choice == "1":
        print("Please enter this information:")
        model = input("Model:")
        # result of input is string so I need cast it to the float
        b = float(input("Price:"))
        c = input("Descirption:")
        d = int(input("Count:"))  # cast to integer

        bike = {
            "model": model,
            "price": b,
            "description": c,
            "count": d
        }
        stock.append(bike)
        print("Successfully added new bike!")
        info_bike(bike)

    elif choice == "2":
        for item in stock:
            info_bike(item)

    elif choice == "q":
        f = open("bikes.json", "w") #removes whole content of the file
        content = json.dumps(stock) # convert list to the json string
        f.write(content) 
        f.close()
        break

    else:
        print("WRONG INPUT!!!")
print("The program has ended")
