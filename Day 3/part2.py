import sys

def main():
    File = open("Day 3\input", 'r')
    Lines = File.readlines()
    zero = []
    one = []
    bin = ""
    bin2 = ""
    newLines = []

    for p in range(0, len(Lines[0]) - 1):
        zero.append("")
        one.append("")

    for x in range(0, len(Lines) - 1):
        for y in range(0, len(Lines[x]) - 1):
            if int(Lines[x][y]) == 0:
                zero[y] = zero[y] + ("0")
            else:
                one[y] = one[y] + ("1")

            # print("zero = ",zero[index], " ", len(zero[index]), "one = ", one[index], " ", len(one[index]))
    for index in range(0, len(Lines[0]) - 1):
        if len(Lines) == 1:
            break
        print(index)
        if len(zero[index]) < len(one[index]):
            print("zero plus petit")
            for t in range(0, len(Lines) - 1):
                print("T = ", t," index = ", index, " ", Lines[t])
                if int(Lines[t][index]) != 0:
                    newLines.append(Lines[t])
                    print("Newlines = ", newLines)
            Lines = newLines
            newLines.clear()
        else:
            print("one plus petit")
            for m in range(0, len(Lines) - 1):
                print("M = ", m," index = ", index, " ", Lines[t])
                if int(Lines[t][index]) != 1:
                    newLines.append(Lines[t])
            Lines = newLines
            newLines.clear()
        print(Lines)

def pop_zero(Lines, index):
    for i in range(0, len(Lines) - 1):
        if Lines[i][index] == 0:
            Lines.pop(i)
    return Lines

def pop_one(Lines, index):
    for i in range(0, len(Lines) - 1):
        if Lines[i][index] == 1:
            Lines.pop(i)
    return Lines

if __name__ == "__main__":
    main()