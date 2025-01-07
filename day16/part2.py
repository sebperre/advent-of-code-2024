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

heapq.heappush(queue, (0, start, 0, 0, 0))

res = None

# Going to the right is clockwise. Going to the left is counterclockwise
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
vis_directions = [">", "v", "<", "^"]

i = 0

n_turns = None
n_straights = None

visited = set()

while queue:
    cost, location, direction, num_turns, num_straights = heapq.heappop(queue)
    if location == end:
        n_turns = num_turns
        n_straights = num_straights
        res = cost
        break
    
    if (location, (direction + 1) % 4) not in visited:
        visited.add((location, (direction + 1) % 4))
        heapq.heappush(queue, (1000 + cost, location, (direction + 1) % 4, num_turns + 1, num_straights))
    if (location, (direction - 1) % 4) not in visited:
        visited.add((location, (direction - 1) % 4))
        heapq.heappush(queue, (1000 + cost, location, (direction - 1) % 4, num_turns + 1, num_straights))

    if grid[location[0] + directions[direction][0]][location[1] + directions[direction][1]] != "#" and ((location[0] + directions[direction][0], location[1] + directions[direction][1]), direction) not in visited:
        visited.add(((location[0] + directions[direction][0], location[1] + directions[direction][1]), direction))
        heapq.heappush(queue, (1 + cost, (location[0] + directions[direction][0], location[1] + directions[direction][1]), direction, num_turns, num_straights + 1))

print(res)
paths = []

def dfs(pos, seq, direction, cost, visited, num_turns, num_straights):
    if pos == end and cost == res:
        print("got a path")
        paths.append(seq)
        return
    if num_straights > n_straights or num_turns > n_turns:
        return
    
    move_dir = (pos[0] + directions[direction][0], pos[1] + directions[direction][1])

    if grid[move_dir[0]][move_dir[1]] != "#" and move_dir not in visited:
        visited.add(move_dir)
        dfs((pos[0] + directions[direction][0], pos[1] + directions[direction][1]), seq + vis_directions[direction], direction, cost + 1, visited, num_turns, num_straights + 1)
        visited.remove(move_dir)

    dir_cc = (direction + 1) % 4
    move_dir_cc = (pos[0] + directions[dir_cc][0], pos[1] + directions[dir_cc][1])

    if grid[move_dir_cc[0]][move_dir_cc[1]] != "#" and move_dir_cc not in visited:
        visited.add(move_dir_cc)
        dfs((move_dir_cc[0], move_dir_cc[1]), seq + vis_directions[dir_cc], dir_cc, cost + 1001, visited, num_turns + 1, num_straights + 1)
        visited.remove(move_dir_cc)

    dir_ccc = (direction - 1) % 4
    move_dir_ccc = (pos[0] + directions[dir_ccc][0], pos[1] + directions[dir_ccc][1])

    if grid[move_dir_ccc[0]][move_dir_ccc[1]] != "#" and move_dir_ccc not in visited:
        visited.add(move_dir_ccc)
        dfs((move_dir_ccc[0], move_dir_ccc[1]), seq + vis_directions[dir_ccc], dir_ccc, cost + 1001, visited, num_turns + 1, num_straights + 1)
        visited.remove(move_dir_ccc)


dfs(start, "", 0, 0, set(), 0, 0)
print(paths)

view_places = set()
view_places.add(start)

for path in paths:
    curr = start
    for c in path:
        if c == ">":
            curr = (curr[0], curr[1] + 1)
        elif c == "<":
            curr = (curr[0], curr[1] - 1)
        elif c == "^":
            curr = (curr[0] - 1, curr[1])
        else:
            curr = (curr[0] + 1, curr[1])
        view_places.add(curr)

print(len(view_places))
    


