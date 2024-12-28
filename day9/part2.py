f = open("testinput.txt")

question = f.readline()

filesystem = []

for i, c in enumerate(question):
    if i % 2 == 0:
        filesystem += [str(i // 2) for _ in range(int(c))]
    else:
        filesystem += list("." * int(c))

print(filesystem)

l, r = 0, len(filesystem) - 1

while l <= r:
    if filesystem[l] == "." and filesystem[r] != ".":
        filesystem[l], filesystem[r] = filesystem[r], filesystem[l]
    elif filesystem[l] != ".":
        l += 1
    elif filesystem[r] == ".":
        r -= 1

ans = 0

for i in range(len(filesystem)):
    if filesystem[i] == ".":
        break
    ans += i * int(filesystem[i])

print(ans)