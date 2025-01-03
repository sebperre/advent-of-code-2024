f = open("input.txt")

lines = f.readlines()

grid = []

i = 0

while i < len(lines):
    if lines[i] == "\n":
        break
    grid.append(list(lines[i].strip()))
    i += 1

i += 1

print(grid)

actions = ""

while i < len(lines):
    actions += lines[i].strip()
    i += 1

print(actions)