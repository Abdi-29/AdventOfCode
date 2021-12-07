file = open("day3.txt", "r")
content = file.readlines()
new_content = {}
for i in range (len(content)):
    new_content[i] = content[i].split('0')
k = 0
for i in new_content:
    if new_content[i][k] == '':
        new_content[i][k] = 0;
        k += 1
    k = 0
    
print(new_content)

print(new_content[0][2])