import json # Imports JSON module
from bike import Bike #import class Bike from file bike
class Warehouse:

    def __init__(self):
        self.stock = self._read_stock()


    def toJSON(self):
        bikes = []
        for bike in self.stock:
            bikes.append(bike.toJSON())
        return bikes


    def _read_stock(self,filename='bikes.json'):

        f = open(filename, "r")
        content = f.read()
        f.close()
        stock_list_bikes=[]
        if content:
            stock_list_dict = json.loads(content) # converts content of json file to python list of dictionaries
            for bike_dict in stock_list_dict:  # convert dictionary to the Bike object
                stock_list_bikes.append(Bike(**bike_dict))
        else:
            stock = []
        return stock_list_bikes

    def _save_stock(self,filename='bikes.json'):
        f = open(filename, "w") #removes whole content of the file
        content = json.dumps(self.toJSON()) # convert list to the json string
        f.write(content)
        f.close()

    def _print_item(self,index):
        bike = self.stock[index]
        bike.print_bike_info()


    def add_item(self,model,price,description,count):
        if self.find_bike_by_model(model)!= -1:
            print(f"This bike {model} exists")
        else:
            bike = Bike(model,price,description,count)
            self.stock.append(bike)
            self._save_stock()

    def change_price(self,model,new_price):
        index  = self.find_bike_by_model(model)
        if(index != -1):
            self.stock[index].change_price(new_price)
        else:
            print(f"We don't have {model} in our warehouse")

    def find_bike_by_model(self,model):
        """ returns index of item if exists or -1 if doesn't"""
        for i in range(len(self.stock)):
            if self.stock[i].model == model:
                return i
        return -1

    def print_all_items(self):
        print("Welcome to the Warehouse:")
        for bike in self.stock:
            bike.print_bike_info()

        print()

if __name__=="__main__":
    my_warehouse = Warehouse()

    my_warehouse.add_item('my_bike1',150,'bla bla',10)
    my_warehouse.add_item('my_bike2',150,'bla bla',10)
    my_warehouse.add_item('my_bike3',150,'bla bla',10)

    my_warehouse.print_all_items()

    my_warehouse.change_price('my_bike1',300)

    my_warehouse.print_all_items()
