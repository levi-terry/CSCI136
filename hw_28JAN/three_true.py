# Author: LDT
# Date: 27JAN2019
# Title: three_true.py
# Purpose: This program implements a function which returns
# True if 1 or 3 of the 3 boolean arguments are True.


# Function to perform the checking of 3 booleans
def three_true(a, b, c):
    if a:
        if b:
            if c:
                return True
            else:
                return False
        elif c:
            return False
        else:
            return True
    elif b:
        if c:
            return False
        else:
            return True
    elif c:
        return True
    else:
        return False


# Testing Code
if __name__ == "__main__":
    t = True
    f = False
    print(three_true(t, t, t))
    print(three_true(t, t, f))
    print(three_true(t, f, t))
    print(three_true(t, f, f))
    print(three_true(f, t, t))
    print(three_true(f, t, f))
    print(three_true(f, f, t))
    print(three_true(f, f, f))
