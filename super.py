class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a Phone")

class SmartPhone(Phone):

    def buy(self):
        print("Buying a smartphone")
        super().buy() # can access parent's method

s= SmartPhone(20000, 'Realme','IMX896')
s.buy()
