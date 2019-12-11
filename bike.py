
import json


class Bike:

    def __init__(self, model, price, colour, size, gender, quantity):
        self.model = model
        self.price = float(price)
        self.colour = colour
        self.size = size
        self.gender = gender
        self.quantity = int(quantity)


    def change_price(self, new_price):
        if(new_price <= 0):
            raise Exception("Price can't be less than 0")
        self.price = new_price

    def change_model(self, new_model):
        self.model = new_model

    def change_colour(self, new_colour):
        self.colour = new_colour

    def change_size(self, new_size):
        self.size = new_size

    def change_gender(self, new_gender):
        self.gender = new_gender

    def increase_quantity(self, quantity):
        self.quantity += quantity #adds to existing increase_quantity

    def decrease_quantity(self, quantity):
        self.quantity -= quantity # decrease that quantity


    def print_bike_info(self):
        print('-'*50)
        print("Model:", self.model)
        print("Price in DKK:", self.price)
        print("Colour:", self.colour)
        print("Size in cm:", self.size)
        print("M for Mænd eller K for Kvinde:", self.gender)
        print("Size in quantity:", self.quantity)
        print('-'*50)

    def toJSON(self): #converts objects to dictionary
        return {
            'model': self.model,
            'price': self.price,
            'colour': self.colour,
            'size': self.size,
            'gender': self.gender,
            'quantity': self.quantity
        }


if __name__ == '__main__':
    bike = Bike('my Bike', 100, 'bla', 123)
    bike2 = Bike(**{
        'model':'my bike 2',
        'price':500,
        'colour':'yellow',
        'size':150,
        'gender':'K',
        'count':10
    })

    f = open('new_bikes.json', "w")  # removes whole content of the file
    content = json.dumps(bike2.toJSON())  # convert list to the json string
    f.write(content)
    f.close()
