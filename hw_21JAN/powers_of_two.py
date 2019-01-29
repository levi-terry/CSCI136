# Author: LDT
# Date: 20JAN2019
# Title: powers_of_two.py
# Purpose: This program is meant to display the powers of two
# up to a user specified number.

# Import Statements
import sys

# Global Variables
num = int(sys.argv[1])

# Iterate through the powers of 2 up to the specified number
if num <= 0:
    pass
else:
    for i in range(num + 1):
        print(2 ** i)
