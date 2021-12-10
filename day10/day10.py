def ft_check(line):
    tot = 0
    j = 0
    for i in reversed (line):
        if j == len(line):
            break
        if i == '(':
            tot += 1
            j += 1
        if i == '[':
            tot += 2
            j += 1
        if i == '{':
            tot += 3
            j += 1
        if i == '<':
            tot += 4
            j += 1 
        if j != len(line):
            tot *= 5
        if j - 1 == len(line):
            if i == '(':
                tot += 1
            elif i == '[':
                tot += 2
            elif i == '{':
                tot += 3
            elif i == '<':
                tot += 4
            break
    return tot

syntax = open("day10.txt").read().split('\n')
s_open = ['(', '[', '{', '<']
s_close = [')', ']', '}', '>']
brakets = {
    '(': ')',
    '{': '}',
    '[': ']',
    '<': '>'
    }
arr = []
arr1 = []
for i in range(len(syntax)):
    check = []
    for j in range(len(syntax[i])):
        if syntax[i][j] in brakets.keys():
            check.append(syntax[i][j])
        else:
            # print(brakets[chr(syntax[i][j])])
            # x = ord(syntax[i][j]) - 1
            # y = ord(check[-1])
            if brakets[check[-1]] == syntax[i][j]:
                check.pop()
                continue
            else:
                arr.append(syntax[i][j])
                break
    
    # another for loop
    arr1.append(check)
# print(arr1)
count = []
# for line in arr:
#     if line == ')':
#         count[0] += 1
#     elif line == ']':
#         count[1] += 1
#     elif line == '}':
#         count[2] += 1
#     elif line == '>':
#         count[3] += 1
# tot = (count[0] * 3) + (count[1] * 57) + (count[2] * 1197) + (count[3] * 25137)
for line in arr1:
    count.append(ft_check(line))
    

# count.sort()
print(count)