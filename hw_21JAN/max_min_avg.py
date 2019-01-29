# Author: LDT
# Date: 21JAN2019
# Title: max_min_avg.py
# Purpose: This program is meant to read integers from STDIN
# and output the maximum, minimum, and average of those integers.

# Import Statements
import sys

# Global Variables
numberList = []

# Read all numbers from stdin, save to numberList
for line in sys.stdin:
    temp = [int(num) for num in line.split()]
    for i in temp:
        numberList.append(i)

# Output max, min, and average
print("Max: %d" % max(numberList))
print("Min: %d" % min(numberList))
print("Average: %d" % (sum(numberList)/len(numberList)))
