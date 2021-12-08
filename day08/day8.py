def get_the_value_5(line, get_1_4):
    if len(get_1_4) == 0:
        return 2
    elif len(get_1_4) == 1:
        return 5
    elif len(get_1_4) == 2:
        return 3

def get_the_value_6(line, get_1_4):
    if len(get_1_4[0]) == 2:
        if (get_1_4[0] not in get_1_4[1]):
            return 6
        elif get_1_4[0] in get_1_4[1]:
            return 9
        return 0
    else:
        if get_1_4[1] not in get_1_4[0]:
            return 6
        elif get_1_4[1][0] in get_1_4[0]:
            return 9
        return 0
# read the file
left_arr = []
right_arr = []
value = 0
for line in open("day8.txt").readlines():
    left, right = line[:-1].split('| ')
    left_list = left[:-1].split(" ")
    right_list = right[:-1].split(" ")
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
""" arr_len = [acedgfb: 8, cdfbe: 5, gcdfa: 2, fbcad: 3,
               dab: 7, cefabd: 9, cdfgeb: 6, cagedb: 0, ab: 1]"""
# create an array of 8 and assegn them with them value
# arr = {"cagedb": 0, "ab": 1, "gcdfa": 2 , "fbcad": 3, "eafb": 4,
#         "cdfbe": 5, "cdfgeb": 6, "dab": 7, "acedgfb": 8, "cefabd": 9}
boards = []
for i in range(len(left_arr)):
    get_1_4 = []
    for lines in left_arr[i]:
        if len(lines) == 2:
            get_1_4.append(lines)
        elif len(lines) == 4:
            get_1_4.append(lines)
    # boards.append(board)
    board = []
    for line in right_arr[i]:
        # for line in lines:
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
    boards.append(board)
print(boards)



