import sys

def main():
    File = open("Day 3\input2", 'r')
    Lines = File.readlines()
    Lines2 = Lines

    for index in range(0, len(Lines[0])):
        zero = 0
        one = 0
        if len(Lines) == 1:
            break
        for item in Lines:
            if item[index] == "0":
                zero += 1
            else:
                one += 1
        newLines = []
        if zero <= one:
            for line in range(0, len(Lines)):
                if Lines[line][index] == "1":
                    newLines.append(Lines[line])
        else:
            for line in range(0, len(Lines)):
                if Lines[line][index] == "0":
                    newLines.append(Lines[line])
        Lines = newLines

    for index in range(0, len(Lines2[0])):
        zero = 0
        one = 0
        if len(Lines2) == 1:
            break
        for item in Lines2:
            if item[index] == "0":
                zero += 1
            else:
                one += 1
        newLines2 = []
        if zero <= one:
            for line in range(0, len(Lines2)):
                if Lines2[line][index] == "0":
                    newLines2.append(Lines2[line])
        else:
            for line in range(0, len(Lines2)):
                if Lines2[line][index] == "1":
                    newLines2.append(Lines2[line])
        Lines2 = newLines2

    oxy = int(Lines[0], 2)
    oxy2 = int(Lines2[0], 2)
    print(oxy * oxy2)


if __name__ == "__main__":
    main()