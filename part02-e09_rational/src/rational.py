#!/usr/bin/env python3

class Rational(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return Rational((self.a * other.b + self.b * other.a), (self.b * other.b))

    def __sub__(self, other):
        return Rational((self.a * other.b - self.b * other.a), (self.b * other.b))

    def __mul__(self, other):
        return Rational((self.a * other.a), (self.b * other.b))

    def __truediv__(self, other):
        return Rational((self.a * other.b), (self.b * other.a))

    def __eq__(self, other):
        return (self.a * other.b) == (self.b * other.a)

    def __ge__(self, other):
        return (self.a * other.b) >= (self.b * other.a)

    def __gt__(self, other):
        return (self.a * other.b) > (self.b * other.a)

    def __le__(self, other):
        return (self.a * other.b) <= (self.b * other.a)

    def __lt__(self, other):
        return (self.a * other.b) < (self.b * other.a)

    def __ne__(self, other):
        return (self.a * other.b) != (self.b * other.a)

    def __str__(self):
        return f"{self.a}/{self.b}"

def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    print(r1*r2)
    print(r1/r2)
    print(r1+r2)
    print(r1-r2)
    print(Rational(1,2) == Rational(2,4))
    print(Rational(1,2) > Rational(2,4))
    print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()

