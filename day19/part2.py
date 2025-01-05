import re
f = open("input.txt")

lines = f.readlines()

towels = lines[0].strip().split(", ")

patterns = [pattern.strip() for pattern in lines[2:]]

memo = {}

def dfs(i, s):
    if i == len(s):
        return 1
    if i in memo:
        return memo[i]
    amount = 0
    for towel in towels:
        if len(s) >= i + len(towel) and s[i:i + len(towel)] == towel:
            amount += dfs(i + len(towel), s)
    memo[i] = amount
    return memo[i]

res = 0

for i, pattern in enumerate(patterns):
    print(f"{i} out of {len(patterns)}")
    memo = {}
    res += dfs(0, pattern)

print(res)