f = open("input.txt")

rules = []
orderings = []
for newline in f:
    if "|" in newline:
        rules.append(newline.strip())
    else:
        break

for newline in f:
    orderings.append(newline.strip())

ans = 0

for ord in orderings:
    ordering = ord.split(",")
    val = True
    for i in range(len(ordering) - 1):
        not_valid = ordering[i + 1] + "|" + ordering[i]
        if not_valid in rules:
            val = False
            break
    if not val:
        for i in range(len(ordering)):
            for j in range(i + 1, len(ordering)):
                not_valid = ordering[j] + "|" + ordering[i]
                if not_valid in rules:
                    temp = ordering[j]
                    ordering[j] = ordering[i]
                    ordering[i] = temp
        ans += int(ordering[len(ordering) // 2])

print(ans)

