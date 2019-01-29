# Author: LDT
# Date: 27JAN2019
# Title: boolean_array.py
# Purpose: This program writes * for True
# and space for False of a 2D array.


# Function to loop through array, assess value
def do_stuff(array):
    for x in array:
        for y in x:
            if y:
                print("*")
            else:
                print(" ")


# Testing Code
if __name__ == "__main__":
    testArray = [[True, False, True, True], [False, True, False, False]]
    do_stuff(testArray)
