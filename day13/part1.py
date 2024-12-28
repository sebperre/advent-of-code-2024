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

memo = None
button_a = None
button_b = None
target = None

def dfs(x, y):
    if x == target[0] and y == target[1]:
        return 0
    if x > target[0] or y > target[1]:
        return float("inf")
    if (x, y) in memo:
        return memo[(x, y)]
    memo[(x, y)] = min(3 + dfs(x + button_a[0], y + button_a[1]), 1 + dfs(x + button_b[0], y + button_b[1]))
    return memo[(x, y)]

ans = 0

for problem in problems:
    memo = {}
    button_a = (int(problem[0][0]), int(problem[0][1]))
    button_b = (int(problem[1][0]), int(problem[1][1]))
    target = (int(problem[2][0]), int(problem[2][1]))

    res = dfs(0, 0)

    if res == float("inf"):
        continue
    ans += res

print(ans)
