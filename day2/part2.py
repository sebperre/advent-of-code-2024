f = open("input.txt")

num_safe = 0

for newline in f:
    newline = newline.strip().split(" ")

    for i in range(len(newline)):
        line = newline.copy()
        del line[i]
        inc = False
        if int(line[0]) < int(line[1]):
            inc = True
        elif int(line[0]) == int(line[1]):
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
            if safe:
                break
            
        else:
            safe = True
            for i in range(len(line) - 1):
                ith = int(line[i])
                ithp = int(line[i+1])
                if ith <= ithp or ith - ithp > 3:
                    safe = False
                    break
            num_safe += safe
            if safe:
                break
print(num_safe)