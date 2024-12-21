import re

f = open("input.txt")

matrix = []
for newline in f:
    matrix.append(list(newline.strip()))

print(matrix)

result = 0

for i in range(len(matrix) - 2):
    for j in range(len(matrix) - 2):
        if matrix[i][j] == "M" and matrix[i + 1][j + 1] == "A" and matrix[i + 2][j + 2] == "S":
            if (matrix[i][j + 2] == "M" and matrix[i + 2][j] == "S") or (matrix[i][j + 2] == "S" and matrix[i + 2][j] == "M"):
                result += 1
        elif matrix[i][j] == "S" and matrix[i + 1][j + 1] == "A" and matrix[i + 2][j + 2] == "M":
            if (matrix[i][j + 2] == "M" and matrix[i + 2][j] == "S") or (matrix[i][j + 2] == "S" and matrix[i + 2][j] == "M"):
                result += 1
        
print(result)