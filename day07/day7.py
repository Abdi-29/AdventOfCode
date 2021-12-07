def get_not_duplicate_crab(crab):
    tmp = []
    for i in crab:
        if i in crab:
            if i not in tmp:
                tmp.append(i)
    return (tmp)

crab = open("day7.txt").readlines()
for i in range(len(crab)):
    crab = [int(x) for x in crab[i].split(',')]

new_crab_list = get_not_duplicate_crab(crab)
arr = [0]*len(new_crab_list)
for i in range(len(new_crab_list)):
    tmp = new_crab_list[i]
    for j in range(len(crab)):
        if crab[j] > tmp:
            tmp1 = crab[j] - tmp
            for k in range(1, tmp1 + 1):
                arr[i] += k
        elif crab[j] < tmp:
            tmp1 = tmp - crab[j]
            for k in range(tmp1 + 1):
                arr[i] += k
for i in arr:
    print(i)
print(min(arr))