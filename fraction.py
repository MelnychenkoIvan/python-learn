class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other_fraction):
        newnum = self.num * other_fraction.den + other_fraction.num * self.den
        newden = self.den * other_fraction.den
        common = gcd(newnum, newden)

        return Fraction(newnum//common, newden//common)


def gcd(m, n):
    while m != 0 and n != 0:
        print(m == 0, n == 0)
        if m > n:
            m = m % n
        else:
            n = n % m

    return m + n
