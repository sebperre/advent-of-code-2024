f = open("testinput3.txt")

content = f.readlines()

a = int(content[0][12:-1])
b = int(content[1][12:-1])
c = int(content[2][12:-1])

operations = [int(x) for x in content[4][9:].split(",")]

print(operations)

def calc_ops(a):
    return ((a % 8) ^ 4 ^ (a >> ((a % 8) ^ 1))) % 8

ans = None

def dfs(i, s):
    global ans
    if ans:
        return
    if i == -1:
        print(f"{s} first answer")
        ans = s
        return
    for a in range(8):
        res = 0
        if a <= 1:
            res = s + "00" + bin(a)[2:]
        elif a <= 3:
            res = s + "0" + bin(a)[2:]
        else:
            res = s + bin(a)[2:]
        
        # print(i, s, res)
        if calc_ops(int(res, 2)) == operations[i]:
            # print("valid", calc_ops(int(res, 2)))
            if ans:
                return
            if a <= 1:
                dfs(i - 1, s + "00" + bin(a)[2:])
            elif a <= 3:
                dfs(i - 1, s + "0" + bin(a)[2:])
            else:
                dfs(i - 1, s + bin(a)[2:])

dfs(len(operations) - 1, "")

print(ans)
