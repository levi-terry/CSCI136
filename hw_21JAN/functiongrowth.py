# Author: LDT
# Date: 20JAN2019
# Title: functiongrowth.py
# Purpose: This program is meant to display a table of different calculations
# on the different powers of two up to 2048.

# Import Statements
import math

# Global Variables
numbers = []  # array to hold numbers
temp = 2  # variable to count up from 2

# Populate numbers array with 2, 4, 8, 16, ... 2048
while temp <= 2048:
    numbers.append(temp)
    temp *= 2

# Loop to iterate through all the numbers
for i in range(11):
    print("log2n:\t\t%d", math.log(2, numbers[i]))
    print("n:\t\t%d", numbers[i])
    print("n log e n:\t%d", (numbers[i] * math.log(math.e, numbers[i])))
    print("n**2:\t\t%d", (numbers[i] ** 2))
    print("n**3:\t\t%d", (numbers[i] ** 3))
    print("2**n:\t\t%d", (2 ** numbers[i]))
