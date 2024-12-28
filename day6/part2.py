import copy
f = open("input.txt")

matrix = []
for newline in f:
    matrix.append(list(newline.strip()))

start_pos = None

for i, row in enumerate(matrix):
    for j, col in enumerate(row):
        if matrix[i][j] == "^":
            start_pos = (i, j)

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
dir_index = 0

positions = []

matrix[start_pos[0]][start_pos[1]] = "*"
curr_pos = start_pos

c = copy.deepcopy(matrix)

while 0 <= curr_pos[0] < len(matrix) and 0 <= curr_pos[1] < len(matrix[0]):
    if matrix[curr_pos[0]][curr_pos[1]] == ".":
        positions.append(curr_pos)
        matrix[curr_pos[0]][curr_pos[1]] = "*"
    elif matrix[curr_pos[0]][curr_pos[1]] == "#":
        curr_pos = (curr_pos[0] - dirs[dir_index][0], curr_pos[1] - dirs[dir_index][1])
        dir_index += 1
        dir_index = dir_index % len(dirs)   
    curr_pos = (curr_pos[0] + dirs[dir_index][0], curr_pos[1] + dirs[dir_index][1])

res = 0

count = 0

for pos_x, pos_y in positions:
    print(f"On {count} out of {len(positions)}")
    dir_index = 0
    matrix = copy.deepcopy(c)
    matrix[pos_x][pos_y] = "#"
    curr_pos = start_pos
    moves = 0
    while 0 <= curr_pos[0] < len(matrix) and 0 <= curr_pos[1] < len(matrix[0]):
        if matrix[curr_pos[0]][curr_pos[1]] == ".":
            matrix[curr_pos[0]][curr_pos[1]] = dir_index
        elif matrix[curr_pos[0]][curr_pos[1]] == "#":
            curr_pos = (curr_pos[0] - dirs[dir_index][0], curr_pos[1] - dirs[dir_index][1])
            dir_index += 1
            dir_index = dir_index % len(dirs)
        elif matrix[curr_pos[0]][curr_pos[1]] == dir_index:
            res += 1
            break
        curr_pos = (curr_pos[0] + dirs[dir_index][0], curr_pos[1] + dirs[dir_index][1])
    matrix[pos_x][pos_y] = "."
    count += 1

print(res)