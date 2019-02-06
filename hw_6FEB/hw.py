# Author: LDT
# Date: 05FEB2019
# Title: hw.py
# Purpose: Various functions as defined.

# Import Statements
from math import acos, cos, sin, sqrt


# returns the unique prime factors of a number as a set, e.g. f(8) = {2}, f(9) = {3}, f(10) = {2, 5}, f(12) = {2, 3}
def prime_set(number):
    s = set()
    for x in range(number + 1):
        if x == 0:
            continue
        else:
            if number % x == 0:
                counter = 0
                for y in range(x):
                    if y == 0:
                        continue
                    else:
                        if x % y == 0:
                            counter += 1
                if counter == 1:
                    s.add(x)
    return s


# returns the unique prime factors as a map of the factor to how many times it is used,
# e.g. f(8) = {2: 3}, f(9) = {3: 2}, f(10) = {2: 1, 5: 1}
def prime_map(number):
    d = {}
    for x in range(number + 1):
        if x == 0:
            continue
        else:
            if number % x == 0:
                counter = 0
                for y in range(x):
                    if y == 0:
                        continue
                    else:
                        if y in d:
                            d[y] += 1
                        if x % y == 0:
                            counter += 1
                if counter == 1:
                    d[x] = 1
    return d


class Location:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def distance_to(self, other):
        distance = 60 * acos(sin(self._x) * sin(other.x) + cos(self._x) * cos(other.x) * cos(self._y - other.y))
        return distance


class Rational:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __add__(self, b):
        x = self._x + b.x
        y = self._y + b.y
        return Rational(x, y)

    def __sub__(self, b):
        x = self._x - b.x
        y = self._y - b.y
        return Rational(x, y)

    def __mul__(self, b):
        x = self._x * b.x
        y = self._y * b.y
        return Rational(x, y)

    def __abs__(self):
        pass

    def __str__(self):
        return '%d/%d' % (self._x, self._y)


class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def distanceTo(self, b):
        distance = sqrt((self._x - b.x) ** 2 + (self._y - b.y) ** 2)
        return distance  # I know this isn't correct, but I'm not making my programming class another math class.

    def __str__(self):
        return "(%d, %d)" % (self._x, self._y)


# Test Code
if __name__ == "__main__":
    print("Testing prime_set() function")
    print(prime_set(90))

    print("Testing prime_map() function")
    print(prime_map(40))

    # FIXME: Add code to test class Location
    # FIXME: Add code to test class Rational
    # FIXME: Add code to test class Point
