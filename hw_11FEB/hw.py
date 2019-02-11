# Author: LDT
# Date: 10FEB2019
# Title: hw.py
# Purpose: Various functions as defined.


# Recursive function that returns the shortest non-empty string in an array
def shortest_string(array):
    return short_helper(array, array[0])


# Recursive helper function
def short_helper(array, shortest):
    if len(array) == 1:
        return shortest
    if len(array[0]) < len(shortest):
        shortest = array[0]
        return short_helper(array[1:], shortest)
    else:
        return short_helper(array[1:], shortest)


# Statistics. Develop a data type for maintaining statistics in a set of floats. Provide a method to add data points and
# methods that return the number of points, the mean, the standard deviation, and the variance. Develop two
# implementations: one whose instance values are the number of points, the sum of the values, and the sum of the squares
# of the values, and another that keeps an array containing all the points. For simplicity, you may take the maximum
# number of points in the constructor. Your first implementation is likely to be faster and use substantially less
# space, but is also likely to be susceptible to round-off error.


# Time. Develop a data type for the time of the day. Provide client methods that return the current hour, minute, and
# second, as well as a __str__() method. Develop two implementations: one that keeps the time as a single int value
# (number of seconds since midnight) and another that keeps three int values, one each for seconds, minutes, and hours.


# Dates. Develop an API for dates (year, month, day). Include methods for comparing two dates chronologically, computing
# the number of days between two dates, determining the day of the week of a given date, and any other operations that
# you think a client might want.


# A StringBuilder class that has an 'add(s)' method that takes a string and stashes it in an array
# and a '__str__' method implementation that joins all the string in the array into one string
# __str__ is called automatically when you call 'str(something)'


# Code Testing
if __name__ == "__main__":
    testArray = ["one", "to", "three", "fourteen", "five"]
    if shortest_string(testArray) == "to":
        print("Function works correctly")
    else:
        print("Need to fix shortest_string()...")
