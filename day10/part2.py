f = open("input.txt")

grid = []
for line in f:
    grid.append(list(line.strip()))

def dfs(i, j, height):
    if grid[i][j] == "9":
        return 1
    
    res = 0

    if i + 1 < len(grid) and grid[i+1][j] == str(height + 1):
        res += dfs(i + 1, j, height + 1)
    if 0 <= i - 1 and grid[i-1][j] == str(height + 1):
        res += dfs(i - 1, j, height + 1)
    if j + 1 < len(grid[0]) and grid[i][j+1] == str(height + 1):
        res += dfs(i, j+1, height + 1)
    if 0 <= j - 1 and grid[i][j-1] == str(height + 1):
        res += dfs(i, j-1, height + 1)

    return res
    
res = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "0":
            res += dfs(i, j, 0)

print(res)