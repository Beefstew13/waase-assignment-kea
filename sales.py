class Sales:

    def __init__(self):
        self.cart = []

    def add_to_cart(self, bike, amount):
        self.cart.append((bike, amount))

    def get_cart(self):
        return self.cart

    def make_purchase(self):
        self.cart = []

    def display_cart(self):
        if(len(self.cart) == 0):
            print("No items in cart!")
        else:
            for bike, amount in self.cart:
                print(
                    f'{bike.model}   {amount}x ${bike.price} = ${amount*bike.price}\n')

    def empty_the_cart(self):
        self.cart = []
