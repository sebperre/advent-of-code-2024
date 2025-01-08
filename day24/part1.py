import re
lines = open("input.txt").readlines()

i = 0

evaluated = {}

while lines[i] != "\n":
    split_line = lines[i].strip().split(": ")
    evaluated[split_line[0]] = int(split_line[1])
    i += 1

pattern = r"(\w+) (\w+) (\w+) -> (\w+)"

expressions = {}

adjacency_dict = {}

i += 1
for line in lines[i:]:
    expression = re.findall(pattern, line)[0]
    if expression[0] not in adjacency_dict:
        adjacency_dict[expression[0]] = set()
    if expression[2] not in adjacency_dict:
        adjacency_dict[expression[2]] = set()
    if expression[3] not in adjacency_dict:
        adjacency_dict[expression[3]] = set()
    adjacency_dict[expression[0]].add(expression[3])
    adjacency_dict[expression[2]].add(expression[3])

    expressions[expression[3]] = (expression[0], expression[2], expression[1])

result = []
visited = set()

def top_sort(curr_node):
    if curr_node in visited:
        return

    visited.add(curr_node)

    for neighbour in adjacency_dict[curr_node]:
        top_sort(neighbour)
    
    result.append(curr_node)
    
for node in adjacency_dict.keys():
    top_sort(node)

for node in reversed(result):
    if node in evaluated:
        continue

    if expressions[node][2] == "AND":
        evaluated[node] = evaluated[expressions[node][0]] & evaluated[expressions[node][1]]
    elif expressions[node][2] == "OR":
        evaluated[node] = evaluated[expressions[node][0]] | evaluated[expressions[node][1]]
    else:
        evaluated[node] = evaluated[expressions[node][0]] ^ evaluated[expressions[node][1]]

i = 0

res = ""

while True:
    if i < 10:
        if "z0" + str(i) in evaluated:
            res = str(evaluated["z0" + str(i)]) + res
        else:
            break
    else:
        if "z" + str(i) in evaluated:
            res = str(evaluated["z" + str(i)]) + res
        else:
            break
    i += 1
print(int(res, 2))