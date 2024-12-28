import re

f = open("input.txt")

problems = []

list_file = f.readlines()

button = r"X\+(\d+), Y\+(\d+)"
target = r"X=(\d+), Y=(\d+)"

i = 0
while i < len(list_file):
    problem = []
    problem.append(re.findall(button, list_file[i])[0])
    problem.append(re.findall(button, list_file[i + 1])[0])
    problem.append(re.findall(target, list_file[i + 2])[0])
    problems.append(problem)
    i += 4

res = 0

for i, problem in enumerate(problems):
    memo = {}

    tx = int(problem[2][0]) + 10000000000000
    ty = int(problem[2][1]) + 10000000000000

    xa = int(problem[0][0])
    xb = int(problem[1][0])

    ya = int(problem[0][1])
    yb = int(problem[1][1])

    if (tx * yb - ty * xb) % (xa * yb - xb * ya) == 0 and (ty * xa - tx * ya) % (xa * yb - xb * ya) == 0:
        res += 3 * ((tx * yb - ty * xb) // (xa * yb - xb * ya)) + ((ty * xa - tx * ya) // (xa * yb - xb * ya))
    # a = (tx * yb - ty * xb) / (xa * yb - xb * ya)
    # b = (ty * xa - tx * ya) / (xa * yb - xb * ya)

print(res)


