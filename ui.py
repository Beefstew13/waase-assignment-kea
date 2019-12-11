from warehouse import Warehouse
from sales import Sales
from finance import Finance


class UserInterface:

    def __init__(self):
        self.warehouse = Warehouse()
        self.sales = Sales()
        self.finance = Finance()

    def add_new_bike(self, model, price, colour, size, gender, quantity):
        self.warehouse.add_item(model, price, colour, size, gender, quantity)

    def display_stock(self):
        self.warehouse.print_all_items()

    # def add_bike_to_cart(self,model,quantity):
        # if self.warehouse.can_buy(model,quantity) :
        # self.sales.add_to_cart(model,quantity)

    def add_to_cart(self):
        bike_model = input("Enter bike model:")

        bike_index = self.warehouse.find_bike_by_model(bike_model)
        if(bike_index == -1):
            print("We don't have that model")
        else:
            bike = self.warehouse.stock[bike_index]
            amount = int(input("How many of bikes would you buy?"))
            if(amount > bike.quantity):
                print("We don't have enough of that model")
            else:
                self.sales.add_to_cart(bike, amount)

    def make_purchase(self):
        cart = self.sales.get_cart()

        if(len(cart) == 0):
            print("No items in cart!")
        else:
            for bike, amount in cart:
                self.warehouse.decrease_quantity_by(bike.model, amount)

            report = self.finance.create_report(cart)
            print(report)

            self.sales.make_purchase()

    def display_cart(self):
        self.sales.display_cart()

    def display_reports(self):
        self.finance.display_reports()

    def empty_the_cart(self):
        self.sales.empty_the_cart()
# if __name__ == '__main__':
    # ui  = UserInterface #create a concrete object

    # if choice =2 '1':
    #     model = input("enter")
    #
    # ui.add_new_bike(model,price,colour,size,gender,quantity)
    #
    # if choice == '2'
    #     ui.add_bike_to_cart()
