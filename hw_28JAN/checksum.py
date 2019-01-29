# Author: LDT
# Date: 27JAN2019
# Title: three_true.py
# Purpose: This program, when given a 10-digit command-line argument,
# returns the checksum of those 10 digits.

# Import Statements
import sys


# Main Code Here
def checksum(x):
    checksumTotal = 0
    counter = 1
    for y in x:
        for z in y:
            if counter % 2 == 0:
                print("This z is %s" % z)
                doubled = int(z) * 2
                print("Doubled is %d" % doubled)
                checksumSingle = (doubled // 10) + (doubled % 10)
                print("double // 10 = %d" % (doubled // 10))
                print("doubled remainder 10 = %d" % (doubled % 10))
                print("checksumSingle = %d" % checksumSingle)
                checksumTotal += checksumSingle
                print("checksumTotal = %d" % checksumTotal)
            else:
                print("This z is %s" % z)
                checksumTotal += int(z)
                print("checksumTotal = %d" % checksumTotal)
    checksumTotal *= 10
    checksumTotal = checksumTotal % 10
    return checksumTotal


if __name__ == "__main__":
    userInput = sys.argv[1:]
    print(userInput)
    print("Checksum =")
    print(checksum(userInput))
    pass
