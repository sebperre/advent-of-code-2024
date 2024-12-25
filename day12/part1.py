f = open("input.txt")

grid = []
for line in f:
    grid.append(list(line.strip()))

visited = set()

def dfs(i, j, c):
    if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] != c:
        return (1, 0)
    if (i, j, c) in visited:
        return (0, 0)

    visited.add((i, j, c))

    down = dfs(i + 1, j, c)
    up = dfs(i - 1, j, c)
    right = dfs(i, j + 1, c)
    left = dfs(i, j - 1, c)

    return (down[0] + up[0] + right[0] + left[0], down[1] + up[1] + right[1] + left[1] + 1)


area_perims = []

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j, grid[i][j]) in visited:
            continue
        area_perims.append(dfs(i, j, grid[i][j]))

res = 0

for area_perim in area_perims:
    res += area_perim[0] * area_perim[1]

print(res)