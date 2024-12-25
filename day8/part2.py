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

for value in antennas.values():
    for i in range(len(value)):
        for j in range(i + 1, len(value)):
            row_diff, col_diff = value[j][0] - value[i][0], value[j][1] - value[i][1]
            antinode_1 = (value[j][0] + row_diff, value[j][1] + col_diff)
            antinode_2 = (value[i][0] - row_diff, value[i][1] - col_diff)

            if 0 <= antinode_1[0] < row_length and 0 <= antinode_1[1] < col_length and matrix[antinode_1[0]][antinode_1[1]] != "#":
                matrix[antinode_1[0]][antinode_1[1]] = "#"
                ans += 1
            if 0 <= antinode_2[0] < row_length and 0 <= antinode_2[1] < col_length and matrix[antinode_2[0]][antinode_2[1]] != "#":
                matrix[antinode_2[0]][antinode_2[1]] = "#"
                ans += 1
print(ans)