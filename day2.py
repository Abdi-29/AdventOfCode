file = open("day2_text.txt", "r")
new_content = {}
content = file.readlines()
for i in range (len(content)):
    new_content[i] = content[i].split(' ')
k = 0
for line, i in new_content.iteritems():
    new_content[line][1] = int(new_content[line][1])

horizontal = 0
depth = 0
aim = 0
for line, i in new_content.iteritems():
    if new_content[line][0] == "forward":
        horizontal += new_content[line][1]
        depth += new_content[line][1] * aim
    elif new_content[line][0] == "down":
        aim += new_content[line][1]
    else:
        aim -= new_content[line][1]
        
print(horizontal * depth)
        