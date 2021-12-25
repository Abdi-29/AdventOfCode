f = open("input.txt").read().strip().split("\n")

vs = []
rights = []

maxj = len(f[0])
maxi = len(f)

for i, line in enumerate(f):
    for j, char in enumerate(line):
        if line[j] == "v":
            vs.append((i, j))
        if line[j] == ">":
            rights.append((i, j))

turn = 0
while True:
    rset = set(rights)
    vset = set(vs)
    moved = 0
    newRights = []
    newVs = []
    for r in rights:
        i, j = r
        nextLoc = (i, (j + 1) % maxj)
        if nextLoc in rset or nextLoc in vset:
            newRights.append(r)
        else:
            newRights.append(nextLoc)
            moved += 1
    rset = set(newRights)
    for v in vs:
        i, j = v
        nextLoc = ((i + 1) % maxi, j)
        if nextLoc in vset or nextLoc in rset:
            newVs.append(v)
        else:
            newVs.append(nextLoc)
            moved += 1
    rights = newRights
    vs = newVs
    turn += 1
    if moved == 0:
        break
print(turn)