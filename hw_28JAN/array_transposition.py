# Author: LDT
# Date: 27JAN2019
# Title: array_transposition.py
# Purpose: This program flips the rows and columns of a 2d array


# Main Code Here
def flip_array(array):
    newArray = ([j][i] for i, j in array)
    return newArray


# For Testing
if __name__ == "__main__":
    someArray = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    testArray = flip_array(someArray)
    for i in testArray:
        for j in i:
            print(j)
