import heapq

f = open("input.txt")

grid = []
for line in f:
    grid.append(list(line.strip()))

start = None
end = None

empty_spots = {}

for i, line in enumerate(grid):
    for j, cell in enumerate(line):
        if grid[i][j] == "#":
            empty_spots[(i, j)] = False
        if cell == "S":
            start = (i, j)
        elif cell == "E":
            end = (i, j)

grid[start[0]][start[1]] = "."
grid[end[0]][end[1]] = "."

########################################################################

# Going to the right is clockwise. Going to the left is counterclockwise
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
dir_vis = [">", "v", "<", "^"]

on_shortest_path = set()

def dijkstra(start, end):
    queue = []
    res = 0

    heapq.heappush(queue, (0, start, 0, ""))

    visited = set()
    visited.add(start)

    while queue:
        cost, location, direction, seq = heapq.heappop(queue)
        if location == end:
            res = cost
            break
        
        dir_cc = (direction + 1) % 4
        spot_cc = (location[0] + directions[dir_cc][0], location[1] + directions[dir_cc][1])
        if grid[spot_cc[0]][spot_cc[1]] != "#" and spot_cc not in visited:
            visited.add(spot_cc)
            heapq.heappush(queue, (1001 + cost, spot_cc, dir_cc, seq + dir_vis[dir_cc]))
        
        dir_ccc = (direction - 1) % 4
        spot_ccc = (location[0] + directions[dir_ccc][0], location[1] + directions[dir_ccc][1])
        if grid[spot_ccc[0]][spot_ccc[1]] != "#" and spot_ccc not in visited:
            visited.add(spot_ccc)
            heapq.heappush(queue, (1001 + cost, spot_ccc, dir_ccc, seq + dir_vis[dir_ccc]))

        spot_str = (location[0] + directions[direction][0], location[1] + directions[direction][1])
        if grid[spot_str[0]][spot_str[1]] != "#" and spot_str not in visited:
            visited.add(spot_str)
            heapq.heappush(queue, (1 + cost, spot_str, direction, seq + dir_vis[direction]))

    return res

min_cost = dijkstra(start, end)
print(min_cost)

