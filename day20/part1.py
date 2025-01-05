from collections import deque

f = open("input.txt")

grid = []

for line in f:
    grid.append(list(line.strip()))

pos_deletions = []

start = None
end = None

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[0]) - 1):
        if grid[i][j] == "#":
            pos_deletions.append((i, j))
        elif grid[i][j] == "S":
            start = (i, j)
        elif grid[i][j] == "E":
            end = (i, j)

grid[end[0]][end[1]] = "."

def bfs():
    queue = deque()
    queue.append((start, 0))
    visited = set()
    visited.add(start)

    while queue:
        node, seconds = queue.popleft()

        if node == end:
            return seconds

        if (node[0] + 1, node[1]) not in visited and grid[node[0] + 1][node[1]] == ".":
            visited.add((node[0] + 1, node[1]))
            queue.append(((node[0] + 1, node[1]), seconds + 1))
        if (node[0] - 1, node[1]) not in visited and grid[node[0] - 1][node[1]] == ".":
            visited.add((node[0] - 1, node[1]))
            queue.append(((node[0] - 1, node[1]), seconds + 1))
        if (node[0], node[1] + 1) not in visited and grid[node[0]][node[1] + 1] == ".":
            visited.add((node[0], node[1] + 1))
            queue.append(((node[0], node[1] + 1), seconds + 1))
        if (node[0], node[1] - 1) not in visited and grid[node[0]][node[1] - 1] == ".":
            visited.add((node[0], node[1] - 1))
            queue.append(((node[0], node[1] - 1), seconds + 1))

unalt_speed = bfs()

print(unalt_speed)
res = 0

for i, pos in enumerate(pos_deletions):
    print(f"{i} out of {len(pos_deletions)}")
    grid[pos[0]][pos[1]] = "."
    alt_speed = bfs()
    grid[pos[0]][pos[1]] = "#"

    if unalt_speed - alt_speed >= 100:
        res += 1

print(res)
