file = open("text.txt", "r")
content = file.readlines()
for i in range(0, len(content)):
    content[i] = int(content[i])
counter = 0
tot_sum = {}
lenght = len(content) - 3
i = 0
while i <= lenght:
    tot_sum[i] = content[i] + content[i + 1] + content[i + 2]
    i += 1
    
for j in range(lenght):
    if tot_sum[j] < tot_sum[j + 1]:
        counter += 1
    # elif tot_sum[j] == tot_sum[j + 1]:
    #     counter = counter
    else:
        counter += 0
print(tot_sum)
print(counter)
    
