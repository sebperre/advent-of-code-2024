import heapq

f = open("input.txt")

grid = []
for line in f:
    grid.append(list(line.strip()))

start = None
end = None

for i, line in enumerate(grid):
    for j, cell in enumerate(line):
        if cell == "S":
            start = (i, j)
        elif cell == "E":
            end = (i, j)

grid[start[0]][start[1]] = "."
grid[end[0]][end[1]] = "."

queue = []

heapq.heappush(queue, (0, start, 0))

res = None

# Going to the right is clockwise. Going to the left is counterclockwise
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

i = 0

visited = set()

while queue:
    cost, location, direction = heapq.heappop(queue)
    if location == end:
        res = cost
        break
    
    if (location, (direction + 1) % 4) not in visited:
        visited.add((location, (direction + 1) % 4))
        heapq.heappush(queue, (1000 + cost, location, (direction + 1) % 4))
    if (location, (direction - 1) % 4) not in visited:
        visited.add((location, (direction - 1) % 4))
        heapq.heappush(queue, (1000 + cost, location, (direction - 1) % 4))

    if grid[location[0] + directions[direction][0]][location[1] + directions[direction][1]] != "#" and ((location[0] + directions[direction][0], location[1] + directions[direction][1]), direction) not in visited:
        visited.add(((location[0] + directions[direction][0], location[1] + directions[direction][1]), direction))
        heapq.heappush(queue, (1 + cost, (location[0] + directions[direction][0], location[1] + directions[direction][1]), direction))

print(res)