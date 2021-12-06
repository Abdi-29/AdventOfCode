# get the mean between x and y, split them and assign the result to the correct value
def get_mean(x, y, check):
    value = (x1 + y1) / 2.0
    value = str(value).replace('.', ',').split(',')
    if check == 0:
        return (int(value[0]))
    else:
        return (int(value[1]))

line_buff = open("day5.txt").readlines()
for i in range(len(line_buff)):
    line_buff[i] = [int(x) for x in line_buff[i].replace(" -> ", ',').split(',')]
# create a bord 10x10 and fill with zero so we can see when it overloops
board = [[0 for x in range(10)] for y in range(10)]
# check the point of x1, y1, x2 and y2
for x in range(len(line_buff)):
    # assign the values
    x1 = line_buff[x][0]
    y1 = line_buff[x][1]
    x2 = line_buff[x][2]
    y2 = line_buff[x][3]
    board[y1][x1] += 1
    board[y2][x2] += 1
    # check if x1 is egual to exit 2 and y2 is bigger than y1
    if x1 == x2 and y2 > y1:
        for y1 in range(y2):
            board[y1][x1] += 1

    elif x1 == x2 and y2 < y1:
        for y2 in range(y1):
            board[y2][x1] += 1

    elif y1 == y2 and x2 > x1:
        for x1 in range(x2):
            board[x1][y1] += 1

    elif y1 == y2 and x2 < x1:
        for x2 in range(x1):
            board[x2][y1] += 1

for o in board:
    print(o)
# for line in line_buff:
#     print (line)