from collections import deque

f = open("testinput.txt")

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

grid[start[0]][start[1]] = "."
grid[end[0]][end[1]] = "."

def print_matrix(m):
    for line in m:
        print(line)

def populate_from_pos(pos):
    populate_grid = [["#" for _ in range(len(grid[0]))] for _ in range(len(grid))]

    queue = deque()
    queue.append((pos, 0))
    visited = set()
    visited.add(pos)

    while queue:
        node, seconds = queue.popleft()
        populate_grid[node[0]][node[1]] = seconds

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
    return populate_grid

grid[start[0]][start[1]] = "."
grid[end[0]][end[1]] = "."

from_start_matrix = populate_from_pos(start)
from_end_matrix = populate_from_pos(end)

unalt_cost = from_start_matrix[end[0]][end[1]]

pos_spots = []

for i in range(1, len(grid) - 1):
    for j in range(1, len(grid) - 1):
        if grid[i][j] == ".":
            pos_spots.append((i, j))

total = 0
tot = len(pos_spots) * len(pos_spots)

res = 0

for i, j in pos_spots:
    for x, y in pos_spots:
        if total % 1000000 == 0:
            print(f"{total}, {tot}")
        if grid[i][j] != "#" and grid[x][y] != "#" and abs(i - x) + abs(j - y) <= 20:
            new_cost = from_start_matrix[i][j] + abs(i - x) + abs(j - y) + from_end_matrix[x][y]
            if unalt_cost - new_cost >= 50:
                res += 1
        total += 1

print(res)