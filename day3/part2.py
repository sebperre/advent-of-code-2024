import re

f = open("input.txt")

result = 0

do_multiplication = True
for newline in f:
    res = re.findall(r"mul\((?P<num1>\d+),(?P<num2>\d+)\)|(do\(\))|(don't\(\))", newline)
    for op in res:
        if op[2] == "do()":
            do_multiplication = True
        elif op[3] == "don't()":
            do_multiplication = False
        else:
            if do_multiplication:
                result += int(op[0]) * int(op[1])


print(result)

    