import sys

if sys.argv[1] == "cat":
    for line in sys.stdin:
        print(line, end='')
elif sys.argv[1] == "head":
    count = 0
    for line in sys.stdin:
        print(line, end='')
        count += 1
        if count == 3:
            break

elif sys.argv[1] == "tail":
    stuff = []
    for line in sys.stdin:
        stuff.append(line)
    print(stuff[-4], end='')
    print(stuff[-3], end='')
    print(stuff[-2], end='')
    print(stuff[-1], end='')

elif sys.argv[1] == "unique":
    newSet = set()
    for line in sys.stdin:
        if line in newSet:
            continue
        else:
            newSet.add(line)
    print(newSet)

elif sys.argv[1] == "count":
    pass

elif sys.argv[1] == "sort":
    pass

else:
    print("Invalid command")
