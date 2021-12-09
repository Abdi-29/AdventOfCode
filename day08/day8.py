def get_the_value_5(line, get_1_4):
    if len(get_1_4[0]) == 2:
        if all(ch in get_1_4[1] for ch in get_1_4[0]):
            tmp = []
            for ch in get_1_4[1]:
                if ch != get_1_4[0][0] and ch != get_1_4[0][1]:
                    tmp.append(ch)
            if tmp[0] in line and tmp[1] in line:
                return (5)
        if all(ch1 in line for ch1 in get_1_4[0]):
            return 3
        return 2
    else:
        if all(ch in get_1_4[0] for ch in get_1_4[1]):
            tmp = []
            for ch in get_1_4[0]:
                if ch != get_1_4[1][0] and ch != get_1_4[1][1]:
                    tmp.append(ch)
            if tmp[0] in line and tmp[1] in line:
                return (5)
        if all(ch in line for ch in get_1_4[1]):
            return 3
        return 2

def get_the_value_6(line, get_1_4):
    if len(get_1_4[0]) == 2:
        if all(ch in get_1_4[1] for ch in get_1_4[0]) and all(ch1 in line for ch1 in get_1_4[1]):
            return 9
        elif all(ch in line for ch in get_1_4[0]):
            return 0
        return 6
    else:
        if all(ch in get_1_4[0] for ch in get_1_4[1]) and all(ch1 in line for ch1 in get_1_4[0]):
            return 9
        elif all(ch in line for ch in get_1_4[1]):
            return 0
        return 6
# read the file
left_arr = []
right_arr = []
value = 0
for line in open("day8.txt").readlines():
    left, right = line[:-1].split('| ')
    left_list = left[:-1].split(" ")
    right_list = right[:].split(" ")
    left_arr.append(left_list)
    right_arr.append(right_list)
# part one
arr_len = [2, 3, 7, 4]
for i in range(0,len(arr_len)):
    for j in right_arr:
       for k in j:
            if len(k) == arr_len[i]:
                value += 1
# part two
boards = []
f_boards = []
for i in range(len(left_arr)):
    get_1_4 = []
    for lines in left_arr[i]:
        if len(lines) == 2:
            get_1_4.append(lines)
        elif len(lines) == 4:
            get_1_4.append(lines)
    board = []
    for line in right_arr[i]:
        value = 0
        if len(line) == 5:
            value = get_the_value_5(line, get_1_4)
        elif len(line) == 6:
            value = get_the_value_6(line, get_1_4)
        elif len(line) == 2:
            value = 1
        elif len(line) == 3:
            value = 7
        elif len(line) == 4:
            value = 4
        elif len(line) == 7:
            value = 8
        else:
            continue
        board.append(value)
    boards = int("".join(str(n) for n in board))
    f_boards.append(boards)
print(sum(f_boards))