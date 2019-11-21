
import json


class Bike:

    def __init__(self, model, price, description, count):
        self.model = model
        self.price = price
        self.description = description
        self.count = count


    def change_price(self, new_price):
        if(new_price <= 0):
            raise Exception("Price can't be less than 0")
        self.price = new_price

    def change_model(self, new_model):
        self.model = new_model

    def change_description(self, new_description):
        self.description = new_description

    def increase_count(self, amount):
        self.count += amount

    def decrease_count(self, amount):
        self.count -= amount

    def print_bike_info(self):
        print('-'*50)
        print("Model:", self.model)
        print("price:", self.price)
        print("description:", self.description)
        print("count:", self.count)
        print('-'*50)

    def toJSON(self):
        return {
            'model': self.model,
            'price': self.price,
            'description': self.description,
            'count': self.count
        }


if __name__ == '__main__':
    bike = Bike('my Bike', 100, 'bla', 123)
    bike2 = Bike(**{
        'model':'my bike 2',
        'price':46,
        'description':'some description',
        'count':45
    })

    f = open('new_bikes.json', "w")  # removes whole content of the file
    content = json.dumps(bike2.toJSON())  # convert list to the json string
    f.write(content)
    f.close()
