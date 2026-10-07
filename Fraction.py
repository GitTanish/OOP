class Fraction:

    def __init__(self, n, d):
        self.num=n
        self.den=d

    def __str__(self):
        return "{}/{}".format(self.num,self.den)

#   operator overloading
    def __add__(self, other): # self-> numerator and denominator, other-> numerator and denominator
        # self -> Fraction object on the left
        # other -> Fraction object on the right
        temp_num = self.num * other.den + other.num * self.den
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num,temp_den)

    def __sub__(self, other):
        temp_num = self.num * other.den - other.num * self.den
        temp_den = self.den * other.den

        return f"{temp_num}/{temp_den}"

    def __mul__(self, other):
        temp_num = self.num  * other.num
        temp_den = self.den * other.den

        return f"{temp_num}/{temp_den}"

    def __truediv__(self, other):

        temp_num = self.num * other.den
        temp_den = self.den * other.num

        return f"{temp_num}/{temp_den}"


print(Fraction)
