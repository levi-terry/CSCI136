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
    print("tail")

else:
    print("Invalid command")
