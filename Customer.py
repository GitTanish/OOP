# pass by reference
class Customer:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

def greet(customer):
    if customer.gender == 'Male' or customer.gender=='male' :
        print('Hello', customer.name,'sir')
    else:
        print('Hello',customer.name,'mam')

    cust2= Customer('Rajesh','male')

    return cust2

cust = Customer('Nilesh', 'Male')
greet(cust)
new_cust= greet(cust)
print(new_cust.name)
