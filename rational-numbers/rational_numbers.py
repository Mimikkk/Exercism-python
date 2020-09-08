from __future__ import division
from math import gcd

class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.__reduce_to_lowest()

    def __reduce_to_lowest(self):
        self.numer //= (gcd_ := gcd(self.numer, self.denom))
        self.denom //= gcd_
        if self.denom < 0:
            self.numer = -self.numer
            self.denom = -self.denom

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        return Rational(self.numer*other.denom + self.denom*other.numer, self.denom*other.denom)

    def __sub__(self, other):
        return Rational(self.numer*other.denom - self.denom*other.numer, self.denom*other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, other.denom * self.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, other.numer * self.denom)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer**power, self.denom**power)

    def __rpow__(self, base):
        return base**(self.numer/self.denom)
