from warehouse import Warehouse

class UserInterface:

    def __init__(self):
        self.warehouse = Warehouse()
        #self.sales = Sales()
        #self.finance = Finance()


    def add_new_bike(self,model,price,colour,size,gender,quantity):
        self.warehouse.add_item(model,price,colour,size,gender,quantity)

    #def add_bike_to_cart(self,model,quantity):
        #if self.warehouse.can_buy(model,quantity) :
            #self.sales.add_to_cart(model,quantity)


    #def make_purchase(self):
        #self.wareheouse.purchase(self.sales.cart)
        #self.sales.purchase()
        #self.finance.create_receipt()


#if __name__ == '__main__':
    #ui  = UserInterface #create a concrete object

    # if choice =2 '1':
    #     model = input("enter")
    # 
    # ui.add_new_bike(model,price,colour,size,gender,quantity)
    #
    # if choice == '2'
    #     ui.add_bike_to_cart()
