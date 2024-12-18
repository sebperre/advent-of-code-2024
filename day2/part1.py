f = open("input.txt")

num_safe = 0

for line in f:
    line = line.strip().split(" ")


    inc = False
    if int(line[0]) < int(line[1]):
        inc = True
    elif int(line[0]) > int(line[1]):
        inc = False
    else:
        continue

    if inc:
        safe = True
        for i in range(len(line) - 1):
            ith = int(line[i])
            ithp = int(line[i+1])
            if ith >= ithp or ithp - ith > 3:
                safe = False
                break
        num_safe += safe
    else:
        safe = True
        for i in range(len(line) - 1):
            ith = int(line[i])
            ithp = int(line[i+1])
            if ith <= ithp or ith - ithp > 3:
                safe = False
                break
        num_safe += safe
print(num_safe)

        