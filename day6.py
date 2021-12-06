###        PART TWO


fish = open("day6.txt").readlines()
for i in range(len(fish)):
    fish = [int(x) for x in fish[i].split(',')]
for j in range(256):
    for i in range(len(fish)):
        if fish[i] == 0:
            fish[i] = 7
            fish.append(8)
        fish[i] -= 1
print(len(fish))

###   PART 1 EXTRAS 

# new = [[0 for x in range(len[fish])] for y1 in range(len(fish))]
        # new.append(i)
# for line in part:
#     row = [int(x) for x in line.split()]
#     board.append(row)
# boards.append(board)
# for board in boards:
#     print(board)
        # if i == 0:
        #     i += 6
            # new.append(8)
# for line in fish:
#     print(line)

###        PART ONE

#fish = open("day6.txt").readlines()
# for i in range(len(fish)):
#     fish = [int(x) for x in fish[i].split(',')]
# print(fish)
# for j in range(80):
#     for i in range(len(fish)):
#         if fish[i] == 0:
#             fish[i] = 7
#             fish.append(8)
#         fish[i] -= 1
#     print(fish)
# print(len(fish))

