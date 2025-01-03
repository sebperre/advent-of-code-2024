f = open("input.txt")

lines = f.readlines()

grid = []

i = 0

while i < len(lines):
    if lines[i] == "\n":
        break
    grid.append(list(lines[i].strip()))
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

curr_pos = start_pos

k = 0
for action in actions:
    if action == "^":
        if grid[curr_pos[0] - 1][curr_pos[1]] == ".":
            grid[curr_pos[0]][curr_pos[1]] = "."
            grid[curr_pos[0] - 1][curr_pos[1]] = "@"
            curr_pos = (curr_pos[0] - 1, curr_pos[1])
        elif grid[curr_pos[0] - 1][curr_pos[1]] == "O":
            i = 1
            while grid[curr_pos[0] - i][curr_pos[1]] == "O":
                i += 1
            if grid[curr_pos[0] - i][curr_pos[1]] == ".":
                grid[curr_pos[0] - i][curr_pos[1]] = "O"
                grid[curr_pos[0]][curr_pos[1]] = "."
                grid[curr_pos[0] - 1][curr_pos[1]] = "@"
                curr_pos = (curr_pos[0] - 1, curr_pos[1])
        elif grid[curr_pos[0] - 1][curr_pos[1]] == "@":
            print("error")
    elif action == "v":
        if grid[curr_pos[0] + 1][curr_pos[1]] == ".":
            grid[curr_pos[0]][curr_pos[1]] = "."
            grid[curr_pos[0] + 1][curr_pos[1]] = "@"
            curr_pos = (curr_pos[0] + 1, curr_pos[1])
        elif grid[curr_pos[0] + 1][curr_pos[1]] == "O":
            i = 1
            while grid[curr_pos[0] + i][curr_pos[1]] == "O":
                i += 1
            if grid[curr_pos[0] + i][curr_pos[1]] == ".":
                grid[curr_pos[0] + i][curr_pos[1]] = "O"
                grid[curr_pos[0]][curr_pos[1]] = "."
                grid[curr_pos[0] + 1][curr_pos[1]] = "@"
                curr_pos = (curr_pos[0] + 1, curr_pos[1])
        elif grid[curr_pos[0] + 1][curr_pos[1]] == "@":
            print("error")
    elif action == ">":
        if grid[curr_pos[0]][curr_pos[1] + 1] == ".":
            grid[curr_pos[0]][curr_pos[1]] = "."
            grid[curr_pos[0]][curr_pos[1] + 1] = "@"
            curr_pos = (curr_pos[0], curr_pos[1] + 1)
        elif grid[curr_pos[0]][curr_pos[1] + 1] == "O":
            i = 1
            while grid[curr_pos[0]][curr_pos[1] + i] == "O":
                i += 1
            if grid[curr_pos[0]][curr_pos[1] + i] == ".":
                grid[curr_pos[0]][curr_pos[1] + i] = "O"
                grid[curr_pos[0]][curr_pos[1]] = "."
                grid[curr_pos[0]][curr_pos[1] + 1] = "@"
                curr_pos = (curr_pos[0], curr_pos[1] + 1)
        elif grid[curr_pos[0]][curr_pos[1] + 1] == "@":
            print("error")
    elif action == "<":
        if grid[curr_pos[0]][curr_pos[1] - 1] == ".":
            grid[curr_pos[0]][curr_pos[1]] = "."
            grid[curr_pos[0]][curr_pos[1] - 1] = "@"
            curr_pos = (curr_pos[0], curr_pos[1] - 1)
        elif grid[curr_pos[0]][curr_pos[1] - 1] == "O":
            i = 1
            while grid[curr_pos[0]][curr_pos[1] - i] == "O":
                i += 1
            if grid[curr_pos[0]][curr_pos[1] - i] == ".":
                grid[curr_pos[0]][curr_pos[1] - i] = "O"
                grid[curr_pos[0]][curr_pos[1]] = "."
                grid[curr_pos[0]][curr_pos[1] - 1] = "@"
                curr_pos = (curr_pos[0], curr_pos[1] - 1)
        elif grid[curr_pos[0]][curr_pos[1] - 1] == "@":
            print("error")
    k += 1

res = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "O":
            res += i * 100 + j

print(res)

