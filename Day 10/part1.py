import sys

def main():
    File = open("Day 10\input", 'r')
    Lines = File.readlines()

    for i in range(len(Lines)):
        Lines[i] = Lines[i][:-1]

    maxLines = len(Lines)
    maxColumn = len(Lines[0])

    illegal = 0

    for x in range(len(Lines)):
        parenthesis = 0
        squaredBrackets = 0
        curlyBrackets = 0
        signs = 0
        for y in range(len(Lines[x])):
            if Lines[x][y] == "(":
                parenthesis +=1
            elif Lines[x][y] == ")":
                parenthesis -=1
            elif Lines[x][y] == "[":
                squaredBrackets +=1
            elif Lines[x][y] == "]":
                squaredBrackets -=1
            elif Lines[x][y] == "{":
                curlyBrackets +=1
            elif Lines[x][y] == "}":
                curlyBrackets -=1
            elif Lines[x][y] == "<":
                signs +=1
            elif Lines[x][y] == ">":
                signs -=1
            if (Lines[x][y] == ")" and (squaredBrackets > 0 or curlyBrackets > 0 or signs > 0):
                break
            if Lines[x][y] == "]" and (parenthesis > 0 or curlyBrackets > 0 or signs > 0):
                break
            if Lines[x][y] == "}" and (parenthesis > 0 or squaredBrackets > 0 or signs > 0):
                break
            if Lines[x][y] == ">" and (parenthesis > 0 or squaredBrackets > 0 or curlyBrackets > 0):
                break
                print(Lines[x][:y], " par :", parenthesis, "squared br :", squaredBrackets, "curl br :", curlyBrackets, "signs :", signs)
        if parenthesis != 0:
            illegal += (abs(parenthesis) * 3)
        if squaredBrackets != 0:
            illegal += (abs(squaredBrackets) * 57)
        if curlyBrackets != 0:
            illegal += (abs(curlyBrackets) * 1197)
        if signs != 0:
            illegal += (abs(signs) * 25137)
    print(illegal)


if __name__ == "__main__":
    main()