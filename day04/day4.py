data = [int(x) for x in open('correct_input_day04.txt', "r").read().split("\n\n")
input_nb = [int(x) for x in data[0].split(',')]
boards = []
for part in data[1:]:
    part = part.split('\n')
    board=[]
    for line in part:
        row = [int(x) for x in line.split()]
        board.append(row)
    boards.append(board)
for board in boards:
    print(board)

def is_bingo(board):
    for line in board:
        if sum(line) == -5:
            return (True)
    for x in range(5):
        total = 0
        for y in range(5):
            total += board[y][x]
        if (total == -5):
            return (True)
    return (False)

def cross_nb(board, nb):
    for y in range(5):
        for x in range(5):
            if (board[y][x] == nb):
                board[y][x] = -1

def get_res(board, nb):
    total = 0
    for y in range(5):
        for x in range(5):
            if (board[y][x] != -1):
                total += board[y][x]
    return (total * nb)

for nb in input_nb:
    for board in boards:
        cross_nb(board, nb)
        if (is_bingo(board)):
            print(get_res(board, nb))
            quit()

