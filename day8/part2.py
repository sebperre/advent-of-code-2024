f = open("input.txt")

matrix = []
for newline in f:
    matrix.append(list(newline.strip()))

antennas = {}

row_length = len(matrix)
col_length = len(matrix[0])

for i in range(row_length):
    for j in range(col_length):
        if matrix[i][j] != ".":
            if matrix[i][j] in antennas:
                antennas[matrix[i][j]].append((i, j))
            else:
                antennas[matrix[i][j]] = [(i, j)]

ans = 0

max_len = max(len(matrix), len(matrix[0]))

for value in antennas.values():
    for i in range(len(value)):
        for j in range(i + 1, len(value)):
            row_diff, col_diff = value[j][0] - value[i][0], value[j][1] - value[i][1]

            for k in range(max_len + 1):
                antinode_pos = (value[j][0] + k * row_diff, value[j][1] + k * col_diff)
                antinode_neg = (value[j][0] - k * row_diff, value[j][1] - k * col_diff)

                if 0 <= antinode_pos[0] < row_length and 0 <= antinode_pos[1] < col_length and matrix[antinode_pos[0]][antinode_pos[1]] != "#":
                    matrix[antinode_pos[0]][antinode_pos[1]] = "#"
                    ans += 1
                if 0 <= antinode_neg[0] < row_length and 0 <= antinode_neg[1] < col_length and matrix[antinode_neg[0]][antinode_neg[1]] != "#":
                    matrix[antinode_neg[0]][antinode_neg[1]] = "#"
                    ans += 1
print(ans)