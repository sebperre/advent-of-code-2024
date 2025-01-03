import collections
import re

file = "input.txt"

grid_size = None

if file == "input.txt":
    grid_size = 71
elif file == "testinput3.txt":
    grid_size = 4
else:
    grid_size = 7

grid = [["." for _ in range(grid_size)] for _ in range(grid_size)]

pattern = r"(\d+),(\d+)"

lines = open(file, "r").readlines()

start_pos = (0, 0)

def bfs():
    visited = set()
    visited.add(start_pos)
    queue = collections.deque()
    queue.append((start_pos, 0))

    found = False

    while queue:
        node, steps = queue.popleft()
        if node[0] == grid_size - 1 and node[1] == grid_size - 1:
            found = True
            break

        if 0 <= node[0] - 1 and grid[node[0] - 1][node[1]] != "#" and (node[0] - 1, node[1]) not in visited:
            visited.add((node[0] - 1, node[1]))
            queue.append(((node[0] - 1, node[1]), steps + 1))
        if node[0] + 1 < grid_size and grid[node[0] + 1][node[1]] != "#" and (node[0] + 1, node[1]) not in visited:
            visited.add((node[0] + 1, node[1]))
            queue.append(((node[0] + 1, node[1]), steps + 1))
        if 0 <= node[1] - 1 and grid[node[0]][node[1] - 1] != "#" and (node[0], node[1] - 1) not in visited:
            visited.add((node[0], node[1] - 1))
            queue.append(((node[0], node[1] - 1), steps + 1))
        if node[1] + 1 < grid_size and grid[node[0]][node[1] + 1] != "#" and (node[0], node[1] + 1) not in visited:
            visited.add((node[0], node[1] + 1))
            queue.append(((node[0], node[1] + 1), steps + 1))
    return found

i = 0

while i < len(lines):
    print(i)
    match = re.findall(pattern, lines[i])[0]
    grid[int(match[1])][int(match[0])] = "#"
    if not bfs():
        break
    i += 1

print(lines[i])