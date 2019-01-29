import sys

numberList = []

numberList.append(sys.argv[1])
numberList.append(sys.argv[2])
numberList.append(sys.argv[3])

if numberList[0] == min(numberList):
    print(numberList[0])
    if numberList[2] == max(numberList):
        print(numberList[1])
        print(numberList[2])
    else:
        print(numberList[2])
        print(numberList[1])
elif numberList[1] == min(numberList):
    print(numberList[1])
    if numberList[0] == max(numberList):
        print(numberList[2])
        print(numberList[0])
    else:
        print(numberList[0])
        print(numberList[2])
else:
    print(numberList[2])
    if numberList[0] == max(numberList):
        print(numberList[1])
        print(numberList[0])
    else:
        print(numberList[0])
        print(numberList[1])
