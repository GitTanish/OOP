# pass by reference
class Customer:
    def __init__(self, name):
        self.name = name


def greet(customer):
    # print(id(customer))
    customer.name = "TySon"
    print(customer.name)
    print(id(customer))

cust=Customer("D'amato")
greet(cust)
print(id(cust))
# they'll have same ID since Reference

# What will be the name?
print(cust.name)
# tip:- same reference
