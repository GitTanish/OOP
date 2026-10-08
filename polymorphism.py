class Phone:
    def __init__(self,price , brand, camera):
        print("Inside Phone Constructor")
        self.price=price
        self.brand=brand
        self.camera = camera

    def buy(self):
        print('Buying a phone')

class SmartPhone(Phone):
    def buy(self):
        print("Buying a smartphone")

s=SmartPhone(20000, 'Realme','IMX896')
print(s.brand)
print(s.camera)
s.buy() # method overriding, child's method will override parent's method
