from heapq import heappop, heappush

def get_neighbour(r, c):
	return [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]

def main():
	level = open("input.txt").readlines()
	g = [[int(x) for x in line.strip()] for line in level]
	queue = [(0, (0, 0))]
	len1 = len(g) - 1
	len2 = len(g[0]) - 1
	end = (len1, len2)
	locked = set()
	while queue:
		risk, position = heappop(queue)
		if position == end:
			break
		if position in locked:
			continue
		locked.add(position)
		for r, c in get_neighbour(*position):
			if 0 <= r < len1 + 1 and 0 <= c < len2 + 1:
				heappush(queue, (risk + g[r][c], (r, c)))
	print(f'part 1: {risk}')
if __name__ == "__main__":
    main()