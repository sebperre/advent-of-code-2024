f = open("input.txt")

res = ""

stones = tuple(f.readline().split(" "))

blinks = 75

memo = {}

def dfs(stones, blink):
    if blink == blinks:
        return len(stones)
    if (stones, blink) in memo:
        return memo[(stones, blink)]
    res = 0
    for stone in stones:
        if stone == "0":
            res += dfs(tuple("1"), blink + 1)
        elif len(stone) % 2 == 0:
            res += dfs((str(int(stone[:(len(stone) // 2)])), str(int(stone[(len(stone) // 2):]))), blink + 1)
        else:
            res += dfs(((str(2024 * int(stone))),), blink + 1)
    memo[(stones, blink)] = res
    return memo[(stones, blink)]

print(dfs(stones, 0))

