import re
f = open("input.txt")

lines = f.readlines()

towels = lines[0].strip().split(", ")

patterns = [pattern.strip() for pattern in lines[2:]]

memo = {}

def dfs(i, s):
    if i == len(s):
        return True
    if i in memo:
        return memo[i]
    valid = False
    for towel in towels:
        if len(s) >= i + len(towel) and s[i:i + len(towel)] == towel:
            valid = valid or dfs(i + len(towel), s)
    memo[i] = valid
    return memo[i]

res = 0

dfs(0, "gbbgrwbbbuwrwwubrgrguwwuwrgbrrwwrbggbrbuwuurggrbwggr")

for i, pattern in enumerate(patterns):
    print(f"{i} out of {len(patterns)}")
    memo = {}
    if dfs(0, pattern):
        res += 1

print(res)