# Author: LDT
# Date: 27JAN2019
# Title: recursion_begin.py
# Purpose: This program implements two functions.
# The first function accepts an int array as a parameter
# and returns the sum of the array using recursion. The
# second function validates nested parentheses oriented
# correctly, such as (), (()()), and so on using recursion


# Int sum w/recursion function
def int_sum(array):
    if len(array) == 0:
        return 0
    else:
        return array[0] + int_sum(array[1:])


# Parentheses function recursion
def parentheses_nesting(string):  # FIXME: Add the code, what to return?
    pass


# Code testing
if __name__ == "__main__":

    # Test int_sum function
    intArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    intArray2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    print("Testing int_sum function on first array...")
    print("Results should read 55:")
    print(int_sum(intArray))
    if int_sum(intArray) == 55:
        print("Success!")
    else:
        print("Need to fix int_sum function...")
    print("Testing int_sum function on second array...")
    print("Results should read 145")
    print(int_sum(intArray2))
    if int_sum(intArray2) == 145:
        print("Success!")
    else:
        print("Need to fix int_sum function...")

    # Test parentheses_nesting function
    paren1 = "()"  # Good
    paren2 = "()()"  # Good
    paren3 = "(()())"  # Good
    paren4 = "((()()()))"  # Good
    paren5 = ")("  # Bad
    paren6 = "(()))())"  # Bad
    print("Testing parentheses_nesting function...")
    print("Results TBD")  # FIXME: Figure out what results should look like after writing code
    print(parentheses_nesting(paren1))
    print(parentheses_nesting(paren2))
    print(parentheses_nesting(paren3))
    print(parentheses_nesting(paren4))
    print(parentheses_nesting(paren5))
    print(parentheses_nesting(paren6))
