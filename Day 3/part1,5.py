import sys

def main():
    File = open("Day 3\input2", 'r')
    Lines = File.readlines()
    zero = []
    one = []
    bin = ""
    bin2 = ""

    for p in range(0, len(Lines[0]) - 1):
        zero.append("")
        one.append("")

    for x in range(0, len(Lines) - 1):
        for y in range(0, len(Lines[x]) - 1):
            if int(Lines[x][y]) == 0:
                zero[y] = zero[y] + ("0")
            else:
                one[y] = one[y] + ("1")

    for u in range(0, len(Lines[0]) - 1):
        if len(zero[u]) < len(one[u]):
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