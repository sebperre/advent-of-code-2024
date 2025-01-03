f = open("input.txt")

grid = []
for line in f:
    grid.append(list(line.strip()))

sides = []
areas = []

visited = set()

def dfs(i, j, c, d, l):
    if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] != c:
        l.add((i, j, d))
        return 0
    if (i, j, c) in visited:
        return 0

    visited.add((i, j, c))

    return dfs(i + 1, j, c, "down", l) + dfs(i - 1, j, c, "up", l) + dfs(i, j + 1, c, "right", l) + dfs(i, j - 1, c, "left", l) + 1

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j, grid[i][j]) in visited:
            continue
        l = set()
        area = dfs(i, j, grid[i][j], "", l)
        if len(l) != 0:
            sides.append(l)
            areas.append(area)

num_sides_list = []

for block in sides:
    visited_block = set()
    num_sides = 0
    for edge in block:
        if edge in visited_block:
            continue
        num_sides += 1
        visited_block.add(edge)
        if edge[2] == "right" or edge[2] == "left":
            i = edge[0]
            while (i - 1, edge[1], edge[2]) in block:
                visited_block.add((i - 1, edge[1], edge[2]))
                i = i - 1
            i = edge[0]
            while (i + 1, edge[1], edge[2]) in block:
                visited_block.add((i + 1, edge[1], edge[2]))
                i = i + 1
        else:
            i = edge[1]
            while (edge[0], i - 1, edge[2]) in block:
                visited_block.add((edge[0], i - 1, edge[2]))
                i = i - 1
            i = edge[1]
            while (edge[0], i + 1, edge[2]) in block:
                visited_block.add((edge[0], i + 1, edge[2]))
                i = i + 1
    num_sides_list.append(num_sides)

res = 0

for i in range(len(num_sides_list)):
    res += areas[i] * num_sides_list[i]

print(res)