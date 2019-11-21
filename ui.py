class UserInterface:

    self __init__(self):
        self.warehouse = Warehouse()
        self.salses = Sales()
        self.finance = Finance()

    
    def add_new_bike(self,model,price,description,count):
        self.warehouse.add_item(model,price,description,count)

    def add_bike_to_cart(self,model,count):
        if self.warehouse.can_buy(model,count) :
            self.sales.add_to_cart(model,count)


    def make_purchase(self):
        self.wareheouse.purchase(self.sales.cart)
        self.sales.purchase()
        self.finacne.create_receipt()


if __name__ == '__main__':
    ui  = UserInterface()

    if choice =2 '1':
        model = input("enter")

    ui.add_new_bike(model,price,...)

    if choice == '2'
        ui.add_bike_to_cart()


