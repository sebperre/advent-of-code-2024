f = open("input.txt", "r")

left = []
right = []

for line in f:
    l_list = line.strip().split("   ")
    left.append(l_list[0])
    right.append(l_list[1])

left.sort()
right.sort()

res = 0

for i in range(len(left)):
    res += abs(int(left[i]) - int(right[i]))

print(res)

