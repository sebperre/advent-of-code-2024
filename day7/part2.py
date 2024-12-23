f = open("input.txt")

ans = 0

for newline in f:
    line = newline.split(":")
    line[1] = line[1].strip().split()
    

    is_valid = False

    def dfs(i, total):
        global is_valid
        if is_valid:
            return
        if i >= len(line[1]):
            if total == int(line[0]):
                is_valid = True
            return
        
        dfs(i+1, total * int(line[1][i]))
        dfs(i+1, total + int(line[1][i]))
        dfs(i+1, int(str(total) + line[1][i]))

    dfs(1, int(line[1][0]))

    if is_valid:
        ans += int(line[0])
  
print(ans)