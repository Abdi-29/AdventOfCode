def check_move_player1(die, position):
    moves = 0
    for i in range (3):
        moves += die + i
    position += moves
    if position > 10:
        position = position % 10
    return position

def get_result(position, point):
    i = 1
    turn = 0
    while i < 99:
        if i > 10:
            i = i % 10
        print("i = ", i)
        if point[0] >= 1000 or point[1] > 1000:
            print(turn * 3)
            return point
        if turn % 2 == 0:
            position[0] = check_move_player1(i, position[0])
            point[0] += position[0]
        else:
            position[1] = check_move_player1(i, position[1])
            point[1] += position[1]
        turn += 1
        i += 3
    return point

def main():
    position = [4, 9]
    point = [0, 0]
    point = get_result(position, point)
    print("point ", point)

if __name__ == "__main__":
    main()