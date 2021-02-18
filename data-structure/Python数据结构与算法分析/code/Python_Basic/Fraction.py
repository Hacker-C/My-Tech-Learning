class Fraction:

    def __init__(self, top, bottom):
        if all([isinstance(x, int) for x in [top, bottom]]):
            common = self.gcd(top, bottom)
            label = (top*bottom)//abs(top*bottom)
            self.num = label * abs(top // common)
            self.den = label * abs(bottom // common)
        else:
            raise TypeError("请传入两个整数")

    def show(self):
        print('{}/{}'.format(self.num, self.den))

    @staticmethod
    def gcd(m, n):
        while m % n != 0:
            oldm = m
            oldn = n
            m = oldn
            n = oldm % oldn
        return n

    def __str__(self):
        if self.num == 0:
            return '0'
        if self.den == 0:
            return '∞'
        if self.num == self.den:
            return '1'
        return "{}/{}".format(self.num, self.den)

    # 加法
    def __add__(self, otherfraction):
        newNum = self.num * otherfraction.den + self.den * otherfraction.num
        newDen = self.den * otherfraction.den
        # common = self.gcd(newNum, newDen)
        # return Fraction(newNum // common, newDen // common)
        return Fraction(newNum, newDen)

    # 减法
    def __sub__(self, otherfraction):
        return self.__add__(Fraction(-otherfraction.num, otherfraction.den))

    # 乘法
    def __mul__(self, otherfraction):
        return Fraction(self.num * otherfraction.num, self.den * otherfraction.den)

    # 除法
    def __truediv__(self, otherfraction):
        return Fraction(self.num * otherfraction.den, self.den * otherfraction.num)

    # 大于
    def __gt__(self, otherfraction):
        return self.num * otherfraction.den > self.den * otherfraction.num

    # 大于等于
    def __ge__(self, otherfraction):
        return self.num * otherfraction.den >= self.den * otherfraction.num

    # 小于
    def __lt__(self, otherfraction):
        return self.num * otherfraction.den < self.den * otherfraction.num

    # 小于等于
    def __le__(self, otherfraction):
        return self.num * otherfraction.den <= self.den * otherfraction.num

    # 等于
    def __eq__(self, otherfraction):
        return self.num * otherfraction.den == self.den * otherfraction.num

    # 不等于
    def __ne__(self, otherfraction):
        return self.num * otherfraction.den != self.den * otherfraction.num

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den


f1 = Fraction(3.2, 7)
f2 = Fraction(1, 7)
# print(f1 != f2)
