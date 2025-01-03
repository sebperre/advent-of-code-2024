import re, math
from functools import reduce

text_input = "input.txt"

pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"

seconds = 1000000

width = 0
height = 0

if text_input == "input.txt":
    width = 101
    height = 103
else:
    width = 11
    height = 7

second = 0
output = open("output.txt", "w")
while second < seconds:
    print(second)
    f = open(text_input)
    invalid = False
    grid = [["." for _ in range(width)] for _ in range(height)]
    for line in f:
        init_x, init_y, vel_x, vel_y = re.findall(pattern, line)[0]
        ending_pos = ((int(init_x) + int(vel_x) * second) % width, (int(init_y) + int(vel_y) * second) % height)
        if grid[ending_pos[1]][ending_pos[0]] == ".":
            grid[ending_pos[1]][ending_pos[0]] = "■"
        else:
            invalid = True
            break
    f.close()
    if invalid:
        second += 1
        continue
    output.write(str(second) + "\n")
    for line in grid:
        for cell in line:
            output.write(cell + " ")
        output.write("\n")
        
    output.write("\n")
    second += 1
    
    








