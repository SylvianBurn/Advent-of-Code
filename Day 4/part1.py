import sys

def main():
    File = open("Day 4\input", 'r')

    Lines = File.read()

    Lines = Lines.split("\n\n")
    bingoNbs = Lines[0].split(",")
    # bingoNbs is the list of all the target numbers

    Lines.pop(0)
    copy = Lines
    #print(Lines)
    # Lines already contains the Bingo boards but as strings

    for boards in range(len(Lines)):
        copy.append("")
        

    Boards = []
    for board in range(0, len(Lines)):
        Boards.append(Lines[board].split("\n"))
        #for
    # print(Boards[0])
    # Each Boards's array contains a board splited in lines

    BoardLines = []
    for lines in range(len(Boards)):
        for line in range(len(Boards[0])):
            BoardLines.append(int(Boards[lines][line].split(" ")))
            if BoardLines[lines][line] == '':
                BoardLines[lines].pop(line)
    print(BoardLines)
    # print(BoardLines)

if __name__ == "__main__":
    main()