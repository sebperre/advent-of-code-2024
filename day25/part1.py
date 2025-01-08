lines = open("input.txt").readlines()

locks = []
keys = []

i = 0
while i < len(lines):
    # Lock
    if lines[i].strip() == "#####":
        i += 1
        lock = [0, 0, 0, 0, 0]
        for j in range(5):
            for k, c in enumerate(lines[i + j].strip()):
                if c == "#":
                    lock[k] += 1
        locks.append(lock)

    # Key
    else:
        i += 1
        key = [5, 5, 5, 5, 5]
        for j in range(5):
            for k, c in enumerate(lines[i + j].strip()):
                if c == ".":
                    key[k] -= 1
        keys.append(key)
    i += 7

res = 0

for lock in locks:
    for key in keys:
        valid = True
        for i in range(5):
            if key[i] + lock[i] > 5:
                valid = False
                break
        if valid:
            res += 1

print(res)

