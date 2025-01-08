import heapq

f = open("testinput2.txt")

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

########################################################################

# Going to the right is clockwise. Going to the left is counterclockwise
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def populate_matrix_from_node(node, matrix):
    queue = []

    heapq.heappush(queue, (0, node, 0))

    visited = set()
    visited.add(node)

    while queue:
        cost, location, direction = heapq.heappop(queue)
        matrix[location[0]][location[1]] = (cost, direction)
        
        dir_cc = (direction + 1) % 4
        spot_cc = (location[0] + directions[dir_cc][0], location[1] + directions[dir_cc][1])
        if grid[spot_cc[0]][spot_cc[1]] != "#" and spot_cc not in visited:
            visited.add(spot_cc)
            heapq.heappush(queue, (1001 + cost, spot_cc, dir_cc))
        
        dir_ccc = (direction - 1) % 4
        spot_ccc = (location[0] + directions[dir_ccc][0], location[1] + directions[dir_ccc][1])
        if grid[spot_ccc[0]][spot_ccc[1]] != "#" and spot_ccc not in visited:
            visited.add(spot_ccc)
            heapq.heappush(queue, (1001 + cost, spot_ccc, dir_ccc))

        spot_str = (location[0] + directions[direction][0], location[1] + directions[direction][1])
        if grid[spot_str[0]][spot_str[1]] != "#" and spot_str not in visited:
            visited.add(spot_str)
            heapq.heappush(queue, (1 + cost, spot_str, direction))

start_pop = [["#" for _ in range(len(grid[0]))] for _ in range(len(grid))]
populate_matrix_from_node(start, start_pop)

end_pop = [["#" for _ in range(len(grid[0]))] for _ in range(len(grid))]
populate_matrix_from_node(end, end_pop)

score = 11048

ans = 0

print(start_pop[14][1], end_pop[14][1])

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "#":
            continue
        if (i, j) == start or (i, j) == end:
            ans += 1
        elif abs(start_pop[i][j][1] - end_pop[i][j][1]) % 2 == 1:
            if start_pop[i][j][0] + end_pop[i][j][0] + 1000 == score:
                ans += 1
        else:
            if start_pop[i][j][0] + end_pop[i][j][0] == score:
                ans += 1
print(ans)

