import re

f = open("testinput.txt")

matrix = []
for newline in f:
    matrix.append(list(newline.strip()))


print("count horizontal")
count_horizontal = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0]) - 3):
        if matrix[i][j] == "X" and matrix[i][j + 1] == "M" and matrix[i][j + 2] == "A" and matrix[i][j + 3] == "S":
            count_horizontal += 1
        if matrix[i][j] == "S" and matrix[i][j + 1] == "A" and matrix[i][j + 2] == "M" and matrix[i][j + 3] == "X":
            count_horizontal += 1
        print(f"Row: {i}, Col: {j} {j + 1} {j + 2} {j + 3}")

print("count vertical")
count_vertical = 0
for i in range(len(matrix) - 3):
    for j in range(len(matrix[0])):
        if matrix[i][j] == "X" and matrix[i + 1][j] == "M" and matrix[i + 2][j] == "A" and matrix[i + 3][j] == "S":
            count_vertical += 1
        if matrix[i][j] == "S" and matrix[i + 1][j] == "A" and matrix[i + 2][j] == "M" and matrix[i + 3][j] == "X":
            count_vertical += 1
        print(f"Row: {i}, {i + 1}, {i + 2}, {i + 3}, Col: {j}")

print("count diag left")
count_diagonal_left = 0
for i in range(len(matrix) - 3):
    for j in range(len(matrix[0]) - 3):
        if matrix[i][j] == "X" and matrix[i + 1][j + 1] == "M" and matrix[i + 2][j + 2] == "A" and matrix[i + 3][j + 3] == "S":
            count_diagonal_left += 1
        if matrix[i][j] == "S" and matrix[i + 1][j + 1] == "A" and matrix[i + 2][j + 2] == "M" and matrix[i + 3][j + 3] == "X":
            count_diagonal_left += 1
        print(f"Coords: ({i}, {j}) ({i + 1}, {j + 1}) ({i + 2}, {j + 2}) ({i + 3}, {j + 3})")

print("count diag right")
count_diagonal_right = 0
for i in range(len(matrix) - 3):
    for j in range(len(matrix[0]) - 3):
        if matrix[i + 3][j] == "X" and matrix[i + 2][j + 1] == "M" and matrix[i + 1][j + 2] == "A" and matrix[i][j + 3] == "S":
            count_diagonal_right += 1
        if matrix[i + 3][j] == "S" and matrix[i + 2][j + 1] == "A" and matrix[i + 1][j + 2] == "M" and matrix[i][j + 3] == "X":
            count_diagonal_right += 1
        # if matrix[i][j] == "X" and matrix[i + 1][j + 1] == "M" and matrix[i + 2][j + 2] == "A" and matrix[i + 3][j + 3] == "S":
        #     count_diagonal_right += 1
        # if matrix[i][j] == "S" and matrix[i + 1][j + 1] == "A" and matrix[i + 2][j + 2] == "M" and matrix[i + 3][j + 3] == "X":
        #     count_diagonal_right += 1
        print(f"Coords: ({i + 3}, {j}) ({i + 2}, {j + 1}) ({i + 1}, {j + 2}) ({i}, {j + 3})")
print(count_horizontal, count_vertical, count_diagonal_left, count_diagonal_right)
print(count_horizontal + count_vertical + count_diagonal_left + count_diagonal_right)
