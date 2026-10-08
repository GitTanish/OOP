class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price=price
        self.brand = brand
        self.camera = camera

class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os ,ram):
        super().__init__(price, brand,camera)
        self.os = os
        self.ram =ram
        print("Inside smartphone constructor")

s=SmartPhone(40000,"Nothing","Lyt700",'Android',8)
print(s.os)
print(s.brand)
