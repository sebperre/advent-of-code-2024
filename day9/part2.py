f = open("input.txt")

question = f.readline()

filesystem = []

for i, c in enumerate(question):
    if i % 2 == 0:
        filesystem += [str(i // 2) for _ in range(int(c))]
    else:
        filesystem += list("." * int(c))

print(filesystem)

r = len(filesystem) - 1


while r >= 0:
    if filesystem[r] == ".":
        r -= 1
    else:
        num_transfer = filesystem[r]
        count = 0
        while r >= 0 and filesystem[r] == num_transfer:
            count += 1
            r -= 1
        l = 0
        placed = False
        while l <= r:
            if filesystem[l] != ".":
                l += 1
            else:
                start = l
                places = 0
                while filesystem[l] == ".":
                    places += 1
                    l += 1
                if places >= count:
                    placed = True
                    end = r + 1
                    while count > 0:
                        filesystem[start] = num_transfer
                        filesystem[end] = "."
                        end += 1
                        start += 1
                        count -= 1
                    break
                if placed:
                    break
        

print(filesystem)

ans = 0

for i in range(len(filesystem)):
    if filesystem[i] == ".":
        continue
    ans += i * int(filesystem[i])

print(ans)