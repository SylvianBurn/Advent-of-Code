import sys

def main():
    File = open("Day 4\input", 'r')

    Lines = File.read()

    Lines = Lines.split("\n\n")
    bingoNbs = Lines[0].split(",")
    # bingoNbs is the list of all the target numbers

    Lines.pop(0)
    #print(Lines)
    # Lines already contains the Bingo boards but as strings
    Boards = []
    for board in range(0, len(Lines)):
        Boards.append(Lines[board].split("\n"))
        for
    #print(Boards)

    BoardLines = []
    for lines in range(len(Boards)):
        for line in range(len(Boards[0])):
            #print(Boards[lines][line])
            BoardLines.append(Boards[lines][line].split(" "))
            BoardLines.strip()
    print(BoardLines)


if __name__ == "__main__":
    main()