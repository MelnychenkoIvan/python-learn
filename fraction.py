class Fraction:
    # Constructor
    def __init__(self, top, bottom):
        common = gcd(top, bottom)
        self.num = top//common
        self.den = bottom//common

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    # toString
    def __str__(self):
        if self.den < 0:
            self.num = -self.num
            self.den = -self.den

        return str(self.num) + '/' + str(self.den)

    # overload p1 + p2
    def __add__(self, other):
        newnum = self.num * other.den + other.num * self.den
        newden = self.den * other.den

        return Fraction(newnum, newden)

    # overload equal
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __sub__(self, other):
        newnum = self.num * other.den - other.num * self.den
        newden = self.den * other.den

        return Fraction(newnum, newden)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den

        return Fraction(newnum, newden)


def gcd(m, n):
    while m != 0 and n != 0:
        if m > n:
            m = m % n
        else:
            n = n % m

    return m + n
