import sys

def main():
    File = open("Day 9\input2", 'r')
    Lines = File.readlines()

    for i in range(len(Lines)):
        Lines[i] = Lines[i][:-1]

    maxLines = len(Lines) - 1
    maxColumn = len(Lines[0]) - 1
    lowPoints = 0

    for i in range(0, maxLines + 1):
        for y in range(0, maxColumn + 1):
            #checking top left corner
            if i == 0 and y == 0:
                if int(Lines[i][y]) < int(Lines[i][y + 1]) and int(Lines[i][y]) < int(Lines[i + 1][y]):
                    lowPoints += int(Lines[i][y]) + 1

            #checking top right corner
            elif i == 0 and y == maxColumn:
                if int(Lines[i][y]) < int(Lines[i][y - 1]) and int(Lines[i][y]) < int(Lines[i + 1][y]):
                    print("I am working")
                    lowPoints += int(Lines[i][y]) + 1

            #checking bottom left corner
            elif i == maxLines and y == 0:
                if int(Lines[i][y]) < int(Lines[i][y + 1]) and int(Lines[i][y]) < int(Lines[i - 1][y]):
                    lowPoints += int(Lines[i][y]) + 1

            #checking bottom right corner
            elif i == maxLines and y == maxColumn:
                if int(Lines[i][y]) < int(Lines[i][y - 1]) and int(Lines[i][y]) < int(Lines[i - 1][y]):
                    lowPoints += int(Lines[i][y]) + 1

            #cheking left column
            elif i > 0 and i < maxLines and y == 0:
                if int(Lines[i][y]) < int(Lines[i - 1][y]) and int(Lines[i][y]) < int(Lines[i][y + 1]) and int(Lines[i][y]) < int(Lines[i + 1][y]):
                    lowPoints += int(Lines[i][y]) + 1

            #checking right column
            elif i > 0 and i < maxLines and y == maxColumn:
                if int(Lines[i][y]) < int(Lines[i - 1][y]) and int(Lines[i][y]) < int(Lines[i][y - 1]) and int(Lines[i][y]) < int(Lines[i + 1][y]):
                    lowPoints += int(Lines[i][y]) + 1

            #checking top line
            elif i == 0 and y > 0 and y < maxColumn:
                if int(Lines[i][y]) < int(Lines[i][y - 1]) and int(Lines[i][y]) < int(Lines[i][y + 1]) and int(Lines[i][y]) < int(Lines[i + 1][y]):
                    lowPoints += int(Lines[i][y]) + 1

            #checking bottom line
            elif i == maxLines and y > 0 and y < maxColumn:
                if int(Lines[i][y]) < int(Lines[i][y - 1]) and int(Lines[i][y]) < int(Lines[i][y + 1]) and int(Lines[i][y]) < int(Lines[i - 1][y]):
                    lowPoints += int(Lines[i][y]) + 1

            #checking everywhere else
            else:
                if int(Lines[i][y]) < int(Lines[i][y - 1]) and int(Lines[i][y]) < int(Lines[i][y + 1]) and int(Lines[i][y]) < int(Lines[i - 1][y]) and int(Lines[i][y]) < int(Lines[i + 1][y]):
                    lowPoints += int(Lines[i][y]) + 1

    print("risk =", lowPoints)

if __name__ == "__main__":
    main()