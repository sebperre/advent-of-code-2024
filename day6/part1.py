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
ans = 1
matrix[start_pos[0]][start_pos[1]] = "*"
curr_pos = start_pos

while 0 <= curr_pos[0] < len(matrix) and 0 <= curr_pos[1] < len(matrix[0]):
    if matrix[curr_pos[0]][curr_pos[1]] == ".":
        ans += 1
        matrix[curr_pos[0]][curr_pos[1]] = "*"
    elif matrix[curr_pos[0]][curr_pos[1]] == "#":
        curr_pos = (curr_pos[0] - dirs[dir_index][0], curr_pos[1] - dirs[dir_index][1])
        dir_index += 1
        dir_index = dir_index % len(dirs)   
    curr_pos = (curr_pos[0] + dirs[dir_index][0], curr_pos[1] + dirs[dir_index][1])

print(matrix)
print(ans)