# collection of objects
class Customer:

    def __init__(self, name,age):
        self.name= name
        self.age= age
    def intro(self):
        print("i AM",self.name,"and I am",self.age)

c1 = Customer('N',23)
c2 = Customer('N',45)
c3 = Customer('N',19)

L=[c1,c2,c3]

for i in L:
    i.intro()
