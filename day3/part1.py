import re

f = open("input.txt")

result = 0

for newline in f:
    res = re.findall(r"mul\((?P<num1>\d+),(?P<num2>\d+)\)", newline)
    for m in res:
        result += int(m[0]) * int(m[1])

print(result)

    