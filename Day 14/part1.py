import sys

def main():
    File = open("Day 14\input", 'r')
    Lines = File.readlines()

    #print(Lines)
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

    for count in range(4):
        for l in range(len(str) - 1):
            for rule in range(0, len(rules)):
                if str[l] == rules[rule][0] and str[l + 1] == rules[rule][1]:
                    str.insert(l + 1, rules[rule][2])
                    print("rule: ", rules[rule], "at l:", l, "str: ", str)
                    l += 1
        print("after step", count + 1, ":", str,"\n")

    print(str)

if __name__ == "__main__":
    main()