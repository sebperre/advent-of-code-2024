import re, math
from functools import reduce

f = open("input.txt")

pattern = r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)"

seconds = 100

width = 101
height = 103

# m = [[0 for _ in range(width)] for _ in range(height)]

quadrants = [0, 0, 0, 0]

# print(width // 2, height // 2, math.ceil(width / 2), )

for line in f:
    init_x, init_y, vel_x, vel_y = re.findall(pattern, line)[0]
    ending_pos = ((int(init_x) + int(vel_x) * 100) % width, (int(init_y) + int(vel_y) * 100) % height)
    # print(ending_pos)
    if ending_pos[0] < width // 2 and ending_pos[1] < height // 2:
        quadrants[0] += 1
    elif ending_pos[0] >= math.ceil(width / 2) and ending_pos[1] < height // 2:
        quadrants[1] += 1
    elif ending_pos[0] < width // 2 and ending_pos[1] >= math.ceil(height / 2):
        quadrants[2] += 1
    elif ending_pos[0] >= math.ceil(width / 2) and ending_pos[1] >= math.ceil(height / 2):
        quadrants[3] += 1 
    # m[ending_pos[1]][ending_pos[0]] += 1

# print(m)
# print(quadrants)
print(reduce(lambda x, y: x * y, quadrants))




