# part two
def doubles(path2):
    for i in path2:
        if i.islower():
            x = path2.count(i)
            if x == 2:
                return (True)
    return (False)

def main():
    caves = open('day12.txt').read().splitlines()
    path = {}
    paths = []
    for line in caves:
        left, right = line.split('-')
        if left not in path:
            path[left] = []
        if right not in path:
            path[right] = []
        if left != 'start' and right != 'end':
            path[right].append(left)
        if right != 'start' and left != 'end':
            path[left].append(right)
    visit_neighbour(path, 'start', 'end', [], paths)
    print(len(paths))
    # print(paths)
# part one
def visit_neighbour(path, start, end, visited, paths):
    visited_copy = visited.copy()
    visited_copy += [start]
    if start == end:
        print(visited_copy)
        paths.append(visited_copy)
        return
        
    for node in path[start]:
        if not node.islower() or node == 'end' or node not in visited_copy or not doubles(visited_copy):
            visit_neighbour(path, node, end, visited_copy, paths)

if __name__ == "__main__":
    main()