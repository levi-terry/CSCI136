# Author: LDT
# Date: 27JAN2019
# Title: checkerboard.py
# Purpose: This program takes the input (n) of a user and creates
# an asterisk checkerboard of size n x n.

# Import Statements
import sys

# Global Variables
userInput = int(sys.argv[1])

# Loop to create n x n checkerboard
for i in range(userInput//2):
    print("* " * userInput)
    print(" *" * (userInput - 1))
if userInput % 2 != 0:
    print("* " * userInput)
