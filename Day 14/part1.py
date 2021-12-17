import sys

def main():
    File = open("Day 14\input2", 'r')
    Lines = File.readlines()

    str = []
    rules = []

    for i in range(len(Lines[0]) - 1):
        str.append(Lines[0][i])

    for x in range(2, len(Lines)):
        tmp =[]
        for y in range(len(Lines[x]) - 1):
            if Lines[x][y].isalpha():
                tmp.append(Lines[x][y])
        rules.append(tmp)


    for count in range(10):
        l = 0
        while l < len(str) - 1:
            for rule in range(len(rules)):
                if str[l] == rules[rule][0] and str[l + 1] == rules[rule][1]:
                    str.insert(l + 1, rules[rule][2])
                    l += 1
                    break
            l += 1

    nbs = []
    for t in range(26):
        nbs.append(0)

    for i in range(len(str)):
        nbs[int(ord(str[i])) - 65] += 1

    nbs = list(filter(lambda num: num != 0, nbs))

    print(max(nbs) - min(nbs))

if __name__ == "__main__":
    main()