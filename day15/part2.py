from collections import deque
f = open("input.txt")

lines = f.readlines()

grid = []

i = 0

while i < len(lines):
    if lines[i] == "\n":
        break
    line = []
    for pos in lines[i].strip():
        if pos == "#":
            line.extend(["#", "#"])
        elif pos == "O":
            line.extend(["[", "]"])
        elif pos == ".":
            line.extend([".", "."])
        else:
            line.extend(["@", "."])

    grid.append(line)
    i += 1

i += 1

actions = ""

while i < len(lines):
    actions += lines[i].strip()
    i += 1

start_pos = None
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "@":
            start_pos = (i, j)

def check_up(i, j):
    queue = deque()
    queue.append((i, j))
    
    visited = set()

    while queue:
        row, col = queue.pop()

        if (row - 1, col) not in visited:
            if grid[row - 1][col] == "[":
                visited.add((row - 1, col))
                visited.add((row - 1, col + 1))
                queue.append((row - 1, col))
                queue.append((row - 1, col + 1))
            elif grid[row - 1][col] == "]":
                visited.add((row - 1, col))
                visited.add((row - 1, col - 1))
                queue.append((row - 1, col))
                queue.append((row - 1, col - 1))
            elif grid[row - 1][col] == "#":
                return False
    return True

def move_up(row, col):
    def dfs(row, col):
        if grid[row - 1][col] == "[":
            dfs(row - 1, col)
        else:
            if grid[row - 1][col - 1] == "[":
                dfs(row - 1, col - 1)
            if grid[row - 1][col + 1] == "[":
                dfs(row - 1, col + 1)

        grid[row - 1][col] = "["
        grid[row - 1][col + 1] = "]"
        grid[row][col] = "."
        grid[row][col + 1] = "."

    if grid[row - 1][col] == "[":
        dfs(row - 1, col)
    elif grid[row - 1][col] == "]":
        dfs(row - 1, col - 1)
    grid[row][col] = "."
    grid[row - 1][col] = "@"

def check_down(i, j):
    queue = deque()
    queue.append((i, j))
    
    visited = set()

    while queue:
        row, col = queue.pop()

        if (row + 1, col) not in visited:
            if grid[row + 1][col] == "[":
                visited.add((row + 1, col))
                visited.add((row + 1, col + 1))
                queue.append((row + 1, col))
                queue.append((row + 1, col + 1))
            elif grid[row + 1][col] == "]":
                visited.add((row + 1, col))
                visited.add((row + 1, col - 1))
                queue.append((row + 1, col))
                queue.append((row + 1, col - 1))
            elif grid[row + 1][col] == "#":
                return False
    return True

def move_down(row, col):
    def dfs(row, col):
        if grid[row + 1][col] == "[":
            dfs(row + 1, col)
        else:
            if grid[row + 1][col - 1] == "[":
                dfs(row + 1, col - 1)
            if grid[row + 1][col + 1] == "[":
                dfs(row + 1, col + 1)

        grid[row + 1][col] = "["
        grid[row + 1][col + 1] = "]"
        grid[row][col] = "."
        grid[row][col + 1] = "."
    
    if grid[row + 1][col] == "[":
        dfs(row + 1, col)
    elif grid[row + 1][col] == "]":
        dfs(row + 1, col - 1)

    grid[row][col] = "."
    grid[row + 1][col] = "@"

curr_pos = start_pos

for action in actions:
    # Up, Down
    if action == "^":
        if grid[curr_pos[0] - 1][curr_pos[1]] == ".":
            grid[curr_pos[0]][curr_pos[1]] = "."
            grid[curr_pos[0] - 1][curr_pos[1]] = "@"
            curr_pos = (curr_pos[0] - 1, curr_pos[1])
        elif grid[curr_pos[0] - 1][curr_pos[1]] in ["[", "]"]:
            if check_up(curr_pos[0], curr_pos[1]):
                move_up(curr_pos[0], curr_pos[1])
                curr_pos = (curr_pos[0] - 1, curr_pos[1])

    elif action == "v":
        if grid[curr_pos[0] + 1][curr_pos[1]] == ".":
            grid[curr_pos[0]][curr_pos[1]] = "."
            grid[curr_pos[0] + 1][curr_pos[1]] = "@"
            curr_pos = (curr_pos[0] + 1, curr_pos[1])
        elif grid[curr_pos[0] + 1][curr_pos[1]] in ["[", "]"]:
            if check_down(curr_pos[0], curr_pos[1]):
                move_down(curr_pos[0], curr_pos[1])
                curr_pos = (curr_pos[0] + 1, curr_pos[1])

    # Left, Right
    elif action == ">":
        if grid[curr_pos[0]][curr_pos[1] + 1] == ".":
            grid[curr_pos[0]][curr_pos[1]] = "."
            grid[curr_pos[0]][curr_pos[1] + 1] = "@"
            curr_pos = (curr_pos[0], curr_pos[1] + 1)


        elif grid[curr_pos[0]][curr_pos[1] + 1] == "[":
            i = 1
            while grid[curr_pos[0]][curr_pos[1] + i] == "[":
                i += 2
            if grid[curr_pos[0]][curr_pos[1] + i] == ".":
                j = 1
                grid[curr_pos[0]][curr_pos[1]] = "."
                grid[curr_pos[0]][curr_pos[1] + j] = "@"
                j += 1
                while j < i:
                    grid[curr_pos[0]][curr_pos[1] + j] = "["
                    grid[curr_pos[0]][curr_pos[1] + j + 1] = "]"
                    j += 2
                
                curr_pos = (curr_pos[0], curr_pos[1] + 1)


    elif action == "<":
        if grid[curr_pos[0]][curr_pos[1] - 1] == ".":
            grid[curr_pos[0]][curr_pos[1]] = "."
            grid[curr_pos[0]][curr_pos[1] - 1] = "@"
            curr_pos = (curr_pos[0], curr_pos[1] - 1)


        elif grid[curr_pos[0]][curr_pos[1] - 1] == "]":
            i = 1
            while grid[curr_pos[0]][curr_pos[1] - i] == "]":
                i += 2
            if grid[curr_pos[0]][curr_pos[1] - i] == ".":
                j = 1
                grid[curr_pos[0]][curr_pos[1]] = "."
                grid[curr_pos[0]][curr_pos[1] - j] = "@"
                j += 1
                while j < i:
                    grid[curr_pos[0]][curr_pos[1] - j] = "]"
                    grid[curr_pos[0]][curr_pos[1] - j - 1] = "["
                    j += 2
                
                curr_pos = (curr_pos[0], curr_pos[1] - 1)

res = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "[":
            res += i * 100 + j

print(res)