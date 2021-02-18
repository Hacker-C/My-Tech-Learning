class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print('{}/{}'.format(self.num, self.den))

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, otherfraction):
        def gcd(m, n):
            while m % n != 0:
                oldm = m
                oldn = n
                m = oldn
                n = oldm % oldn
            return n

        newNum = self.num * otherfraction.den + self.den * otherfraction.num
        newDen = self.den * otherfraction.den
        comon = gcd(newNum, newDen)
        return Fraction(newNum // comon, newDen // comon)

    def __eq__(self, otherfraction):
        return self.num * otherfraction.den == self.den * otherfraction.num


f1 = Fraction(2, 3)
f2 = Fraction(2, 4)
ans = f1 + f2
print(ans)
f3 = Fraction(3, 7)
f4 = Fraction(3, 7)
print(f3==f4)