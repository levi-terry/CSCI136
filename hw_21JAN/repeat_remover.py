# Author: LDT
# Date: 21JAN2019
# Title: repeat_remover.py
# Purpose: This program is meant to read in a sequence of integers and
# write those integers to the screen, removing any duplicates

# Import statements
import sys

# Global Variables
numberList = []

# Iterate through input, comparing ints to see if they are
# equivalent to the last number in numberList array. If they are not,
# write them to the array.
for line in sys.stdin:
    temp = [int(num) for num in line.split()]
    for num in temp:
        if not numberList:
            numberList.append(num)
        else:
            if num == numberList[-1]:
                continue
            else:
                numberList.append(num)

print(numberList)

