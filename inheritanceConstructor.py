class Phone:
    def __init__(self,price , brand, camera):
        print("Inside Phone Constructor")
        self.price=price
        self.brand=brand
        self.camera = camera

class SmartPhone(Phone):
    pass

s=SmartPhone(20000, 'Realme','IMX896')
print(s.brand)
print(s.camera)
