import sys
from typing import NoReturn

def main(argv):
    LargerThanPrevious = 0
    File = open("input", 'r')
    Numbers = File.readlines()
    x = 0
    y = 0
    sum = 0
    list = []

    for x in range(0, len(Numbers) - 2):
        sum = int(Numbers[x]) + int(Numbers[x + 1]) + int(Numbers[x + 2])
        list.append(sum)
        sum = 0

    Numbers = list

    for i in range(1, len(Numbers)):
        if int(Numbers[i - 1]) < int(Numbers[i]):
            LargerThanPrevious += 1

    print(LargerThanPrevious)

if __name__ == "__main__":
    main(sys.argv)