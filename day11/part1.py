f = open("input.txt")

res = ""

res = f.readline().split(" ")

blinks = 75

memo = {}

for blink in range(blinks):
    new_stones = []
    for stone in res:
        if stone == "0":
            new_stones.append("1")
        elif len(stone) % 2 == 0:
            new_stones.append(str(int(stone[:(len(stone) // 2)])))
            new_stones.append(str(int(stone[(len(stone) // 2):])))
        else:
            new_stones.append(str(2024 * int(stone)))
    res = new_stones

print(len(res))

