import sys

def main():
    File = open("Day 3\input2.txt", 'r')
    Lines = File.readlines()
    zero1 = 0
    one1 = 0
    zero2 = 0
    one2 = 0
    zero3 = 0
    one3 = 0
    zero4 = 0
    one4 = 0
    zero5 = 0
    one5 = 0
    zero6 = 0
    one6 = 0
    zero7 = 0
    one7 = 0
    zero8 = 0
    one8 = 0
    zero9 = 0
    one9 = 0
    zero10 = 0
    one10 = 0
    zero11 = 0
    one11 = 0
    zero12 = 0
    one12 = 0
    bin = ""
    bin2 = ""

    for x in range(0, len(Lines)):
        if int(Lines[x][0]) == 0:
            zero1 += 1
        elif int(Lines[x][0]) == 1:
            one1 += 1
        if int(Lines[x][1]) == 0:
            zero2 += 1
        elif int(Lines[x][1]) == 1:
            one2 += 1
        if int(Lines[x][2]) == 0:
            zero3 += 1
        elif int(Lines[x][2]) == 1:
            one3 += 1
        if int(Lines[x][3]) == 0:
            zero4 += 1
        elif int(Lines[x][3]) == 1:
            one4 += 1
        if int(Lines[x][4]) == 0:
            zero5 += 1
        elif int(Lines[x][4]) == 1:
            one5 += 1
        if int(Lines[x][5]) == 0:
            zero6 += 1
        elif int(Lines[x][5]) == 1:
            one6 += 1
        if int(Lines[x][6]) == 0:
            zero7 += 1
        elif int(Lines[x][6]) == 1:
            one7 += 1
        if int(Lines[x][7]) == 0:
            zero8 += 1
        elif int(Lines[x][7]) == 1:
            one8 += 1
        if int(Lines[x][8]) == 0:
            zero9 += 1
        elif int(Lines[x][8]) == 1:
            one9 += 1
        if int(Lines[x][9]) == 0:
            zero10 += 1
        elif int(Lines[x][9]) == 1:
            one10 += 1
        if int(Lines[x][10]) == 0:
            zero11 += 1
        elif int(Lines[x][10]) == 1:
            one11 += 1
        if int(Lines[x][11]) == 0:
            zero12 += 1
        elif int(Lines[x][11]) == 1:
            one12 += 1
    if zero1 < one1:
        bin = bin + "1"
        bin2 = bin2 + "0"
    else:
        bin = bin + "0"
        bin2 = bin2 + "1"
    if zero2 < one2:
        bin = bin + "1"
        bin2 = bin2 + "0"
    else:
        bin = bin + "0"
        bin2 = bin2 + "1"
    if zero3 < one3:
        bin = bin + "1"
        bin2 = bin2 + "0"
    else:
        bin = bin + "0"
        bin2 = bin2 + "1"
    if zero4 < one4:
        bin = bin + "1"
        bin2 = bin2 + "0"
    else:
        bin = bin + "0"
        bin2 = bin2 + "1"
    if zero5 < one5:
        bin = bin + "1"
        bin2 = bin2 + "0"
    else:
        bin = bin + "0"
        bin2 = bin2 + "1"
    if zero6 < one6:
        bin = bin + "1"
        bin2 = bin2 + "0"
    else:
        bin = bin + "0"
        bin2 = bin2 + "1"
    if zero7 < one7:
        bin = bin + "1"
        bin2 = bin2 + "0"
    else:
        bin = bin + "0"
        bin2 = bin2 + "1"
    if zero8 < one8:
        bin = bin + "1"
        bin2 = bin2 + "0"
    else:
        bin = bin + "0"
        bin2 = bin2 + "1"
    if zero9 < one9:
        bin = bin + "1"
        bin2 = bin2 + "0"
    else:
        bin = bin + "0"
        bin2 = bin2 + "1"
    if zero10 < one10:
        bin = bin + "1"
        bin2 = bin2 + "0"
    else:
        bin = bin + "0"
        bin2 = bin2 + "1"
    if zero11 < one11:
        bin = bin + "1"
        bin2 = bin2 + "0"
    else:
        bin = bin + "0"
        bin2 = bin2 + "1"
    if zero12 < one12:
        bin = bin + "1"
        bin2 = bin2 + "0"
    else:
        bin = bin + "0"
        bin2 = bin2 + "1"

    gama = int(bin, 2)
    epsilon = int(bin2, 2)
    print(gama * epsilon)

if __name__ == "__main__":
    main()