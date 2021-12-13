def main():
    paper = open('input.txt').read().splitlines()
    line = []
    max_value = [1311, 895]
    for i in range(len(paper)):
        line.append([int(x) for x in paper[i].split(',')])
    # x_max = []
    # y_max = []
    # for i in line:
    #     x_max.append(i[0])
    #     y_max.append(i[1])
    # print(max(x_max), max(y_max))
    board = [['.' for x in range(max_value[0])] for y in range(max_value[1])]
    fill_the_board(line, board, max_value)

def fill_the_board(paper, board, max_value):
    for x in range(len(paper)):
        for y in range(1):
            i = paper[x][1]
            j = paper[x][0]
            board[i][j] = '#'
    board = fold_vert(board, max_value[1], paper)
    board = fold_horiz(board, max_value[0], paper)
    count = 0
    for line in board:
        print(line[:5])
    for line in board:
        for j in line:
            if j == '.':
                count += 1

def fold_vert(board, v, paper):
    for y in range(v):
        board[v][y] = '-'
    for i in paper:
        if i[1] > v:
            x = i[0]
            y = v - (i[1] - v)
            board[y][x] = '#'
    return(board[:v])

def fold_horiz(board, h, paper):
    new_input = get_new_value(board)
    print(new_input)
    for y in range(7):
        board[y][h] = '|'
    for i in new_input:
        x = h - (i[0] - h)
        y = i[1]
        board[y][x] = '#'
    return(board[:])

def get_new_value(board):
    new_input= []
    count = 0
    line = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '#':
                count += 1
                new_input.append(str(j) + ',' + str(i))
    for i in range(len(new_input)):
        line.append([int(x) for x in new_input[i].split(',')])
    print(count)
    return line
if __name__ == "__main__":
    main()
    