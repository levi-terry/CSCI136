# Author: LDT
# Date: 27JAN2019
# Title: bool_exercise.py
# Purpose: This program is comprised of several functions.
# The any() function evaluates an array of booleans and
# returns True if any boolean is True. The all() function
# evaluates an array of booleans and returns True if all
# are True.


# Function to evaluate if any values in an array are true
def any(booleanArray):
    for i in booleanArray:
        if i:
            return True
        else:
            return False


# Function to evaluate if all values in an array are true
def all(booleanArray):
    flag = True
    for i in booleanArray:
        if not i:
            flag = False
    return flag


# Code Testing
if __name__ == "__main__":
    trueArray = [True, True, True, True]
    tfArray = [True, False, True, False]
    falseArray = [False, False, False, False]

    print("This should return True: ", end='')
    print(any(trueArray))
    print("This should return True: ", end='')
    print(any(tfArray))
    print("This should return False: ", end='')
    print(any(falseArray))
    print("This should return True: ", end='')
    print(all(trueArray))
    print("This should return False: ", end='')
    print(all(tfArray))
    print("This should return False: ", end='')
    print(all(falseArray))
