f = open("testinput.txt")

grid = []
for line in f:
    grid.append(list(line.strip()))

start = None
end = None

for i, line in enumerate(grid):
    for j, cell in enumerate(line):
        if cell == "S":
            start = (i, j)
        elif cell == "E":
            end = (i, j)

memo = {}

def dfs(i, j, dir):
    if grid[i + 1][j]
    dfs()