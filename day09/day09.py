# left up corner
def left_up_corner(actual_nb, right_nb, bottom_nb):
    if actual_nb < right_nb and actual_nb < bottom_nb:
        return True
    return False
# middle up edges
def middle_up_edge(actual_nb, right_nb, bottom_nb, left_nb):
    if actual_nb < right_nb and actual_nb < bottom_nb and actual_nb < left_nb:
        return True
    return False
# right up corner
def right_up_corner(actual_nb, left_nb, bottom_nb):
    if actual_nb < left_nb and actual_nb < bottom_nb:
        return True
    return False
# left middle edges
def middle_left_edge(actual_nb, right_nb, bottom_nb, up_nb):
    if actual_nb < right_nb and actual_nb < bottom_nb and actual_nb < up_nb:
        return True
    return False
# right middle edges
def middle_right_edge(actual_nb, right_nb, bottom_nb, up_nb):
    if actual_nb < right_nb and actual_nb < bottom_nb and actual_nb < up_nb:
        return True
    return False
# middle
def middle(actual_nb, left_nb, right_nb, up_nb, down_nb):
    if actual_nb < left_nb and actual_nb < right_nb and actual_nb < up_nb and actual_nb < down_nb:
        return True
    return False
# left bottom edge
def left_bottom_edge(actual_nb, up_nb, right_nb):
    if actual_nb < up_nb and actual_nb < right_nb:
        return True
    return False
# meddle edge
def middle_bottom_edge(actual_nb, left_nb, right_nb, up_nb):
    if actual_nb < left_nb and actual_nb < right_nb and  actual_nb < up_nb:
        return True
    return False
# right bottom edge
def right_bottom_edge(actual_nb, left_nb, up_nb):
    if actual_nb < left_nb and actual_nb < up_nb:
        return True
    return False

caves = open("day09.txt").read().split('\n')
# part one
result = []
for i in range(len(caves)):
    for j in range(len(caves[i])):
        # check left corner
        num = 0
        if i == 0 and j == 0:
            if left_up_corner(caves[i][j], caves[i][j + 1], caves[i + 1][j]):
                num = int(caves[i][j]) + 1
        # check middle edge
        elif i == 0 and j > 0 and j != len(caves[i]) - 1:
            if middle_up_edge(caves[i][j], caves[i][j + 1], caves[i + 1][j], caves[i][j - 1]):
                num = int(caves[i][j]) + 1
        # check right corner
        elif i == 0 and j == len(caves[i]) - 1:
            if right_up_corner(caves[i][j], caves[i][j - 1], caves[i + 1][j]):
                num = int(caves[i][j]) + 1
        # check middle left edge
        elif i > 0 and j == 0 and i != len(caves) - 1:
            if middle_left_edge(caves[i][j], caves[i][j + 1], caves[i + 1][j], caves[i - 1][j]):
                num = int(caves[i][j]) + 1
        # check middle right edge
        elif i > 0 and j == len(caves[i]) - 1 and i != len(caves) - 1:
            if middle_right_edge(caves[i][j], caves[i][j - 1], caves[i + 1][j], caves[i - 1][j]):
                num = int(caves[i][j]) + 1
        # check middle
        elif i > 0 and j != len(caves[i]) - 1 and i != len(caves) - 1 and j > 0:
            if middle(caves[i][j], caves[i][j - 1], caves[i][j + 1], caves[i - 1][j], caves[i + 1][j]):
                num = int(caves[i][j]) + 1
        # check left bottom edge
        elif i == len(caves) - 1 and j == 0 and j != len(caves[i]) - 1:
            if left_bottom_edge(caves[i][j], caves[i - 1][j], caves[i][j + 1]):
                num = int(caves[i][j]) + 1
        # check middle edge
        elif i == len(caves) - 1 and j > 0 and j != len(caves[i]) - 1:
            if middle_bottom_edge(caves[i][j], caves[i][j - 1], caves[i][j + 1], caves[i - 1][j]):
                num = int(caves[i][j]) + 1
        # right middle bottom
        elif i == len(caves) - 1 and j == len(caves[i]) - 1:
            if right_bottom_edge(caves[i][j], caves[i][j - 1], caves[i - 1][j]):
                num = int(caves[i][j]) + 1
        if num != 0:
            result.append(num)
print(sum(result))