f = open("input.txt", "r")

left = []
d = {}

for line in f:
    l_list = line.strip().split("   ")
    left.append(l_list[0])
    if l_list[1] not in d:
        d[l_list[1]] = 1
    else:
        d[l_list[1]] += 1

res_sim = 0

for num in left:
    if num in d:
        res_sim += int(num) * d[num]

print(res_sim)
