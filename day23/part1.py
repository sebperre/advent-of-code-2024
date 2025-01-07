f = open("input.txt")

connections = []

for line in f:
    connections.append(tuple(line.strip().split("-")))

vertices = set()

for connection in connections:
    vertices.add(connection[0])
    vertices.add(connection[1])

vertices = list(vertices)

adjacency_dict = {vertex: set() for vertex in vertices}

for connection in connections:
    adjacency_dict[connection[0]].add(connection[1])
    adjacency_dict[connection[1]].add(connection[0])

result = 0

for i in range(len(vertices)):
    for j in range(i + 1, len(vertices)):
        for k in range(j + 1, len(vertices)):
            if (vertices[j] in adjacency_dict[vertices[i]] and vertices[k] in adjacency_dict[vertices[i]]) and (vertices[i] in adjacency_dict[vertices[j]] and vertices[k] in adjacency_dict[vertices[j]]) and (vertices[i] in adjacency_dict[vertices[k]] and vertices[j] in adjacency_dict[vertices[k]]):
                if vertices[i][0] == "t" or vertices[j][0] == "t" or vertices[k][0] == "t":
                    result += 1

print(result)
