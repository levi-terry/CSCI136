# Author: LDT
# Date: 3FEB2019
# Title: hw.py
# Description: This program consists of several recursive functions.


# Takes strings s, x, y and returns string with all instances of x replaced with y in s
def replacer(s, x, y):
    if s == '':
        return s
    if s[0] == x:
        return y + replacer(s[1:], x, y)
    return s[0] + replacer(s[1:], x, y)


# Takes an array of ints, returns an array of all the even ints
def evens(array):
    if not array:
        return ''
    if int(array[0]) % 2 == 0:
        return array[0] + evens(array[1:])
    else:
        return evens(array[1:])


# Takes a string, removes duplicates in the string
def remover(s):
    for i in range(len(s)):
        if i == len(s) - 1:
            return s
        if s[i] == s[i+1]:
            return remover(s[:i] + s[i+1:])


# Same as remover, but also adds how many duplicates existed in #
def remover_counter(s):
    for i in range(len(s)):
        if i == len(s) - 1:
            return s
        if s[i] == s[i + 1]:
            return remover(s[:i] + s[i + 1:])


def remover_counter_helper(s, count):
    pass


# For Testing
if __name__ == "__main__":

    # Testing replacer() function
    something = "abracadabra"
    something2 = "b"
    something3 = "d"

    print("Testing replacer function")
    print("Original string is: %s" % something)
    print("New string should be: adracadadra")
    print("New string below:")
    print(replacer(something, something2, something3))
    if replacer(something, something2, something3) == "adracadadra":
        print("Success!")
    else:
        print("Re-evaluate the replacer() function")

    # Testing evens() function
    array1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    print("Testing evens() function")
    print("Original array is:")
    for i in array1:
        print(i, end=' ')
    print("\nNew array should be: [0, 2, 4, 6, 8]")
    newArray = (evens(array1))
    for i in newArray:
        print(i, end=' ')
    print()

    # Testing remover() function
    testString = "ffoobbaaquuuuuuxax"
    print("Testing remover() function")
    print(remover(testString))
