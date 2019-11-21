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
    print()
    print('-'*50)
    print()
    print("Press 1: To add stock\n")
    print("Press 2: To check stock\n")
    print("Press 3: To enter purchase\n")
    print("Press q: To quit the program\n")
    print('-'*50)
    print()
    return input("Please enter your choice: ")


# DRY Don't repeat yourself!
while True:
    choice = menu()
    if choice == "1":
        print("""
--------------------------------------------------

Please enter this information:

--------------------------------------------------
""")
        model = input("Model:\n")
        # result of input is string so I need cast it to the float
        b = float(input("\nPrice:\n"))
        c = input("\nDescirption:\n")
        d = int(input("\nCount:\n"))  # cast to integer

        bike = {
            "model": model,
            "price": b,
            "description": c,
            "count": d
        }
        stock.append(bike)
        print("Successfully added new bike(s)!")
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
