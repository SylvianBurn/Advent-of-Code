import sys

def main():
    total = 0
    File = open("Day 2\input", 'r')
    Lines = File.readlines()
    position = 0
    depth = 0
    aim = 0

    for x in range(0, len(Lines)):
        Lines[x].strip("\n")
        if Lines[x].__contains__("forward"):
            position += int(Lines[x][-2])
            depth += (int(Lines[x][-2]) * aim)
        if Lines[x].__contains__("down"):
            aim += int(Lines[x][-2])
        if Lines[x].__contains__("up"):
            aim -= int(Lines[x][-2])
    total = position * depth
    print(total)

if __name__ == "__main__":
    main()