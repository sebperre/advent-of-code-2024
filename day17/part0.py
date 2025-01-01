f = open("testinput3.txt")

content = f.readlines()

a = int(content[0][12:-1])
b = int(content[1][12:-1])
c = int(content[2][12:-1])

def calc_ops(a):
    return ((a % 8) ^ 4 ^ (a >> ((a % 8) ^ 1))) % 8


while a != 0:
    print(calc_ops(a), end=",")
    a = a >> 3

print("\n")

