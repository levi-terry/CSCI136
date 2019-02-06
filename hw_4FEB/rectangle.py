# Author: LDT
# Date: 3FEB2019
# Title: hw.py
# Purpose: Drawing some rectangles


class Rectangle:
    # Create rectangle w/ center (x, y), width w, and height h.
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    def perimeter(self):
        return (self.w * 2) + (self.h * 2)

    def intersects(self, other):
        pass

    def contains(self, other):
        pass


if __name__ == "__main__":
    pass
