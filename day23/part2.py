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

cliques = []

def bron_kerbosch(R, P, X, graph):
    if not P and not X:
        cliques.append(R.copy())
    copy_x = X.copy()
    copy_p = P.copy()
    for v in P:
        bron_kerbosch(R.copy().union({v}), copy_p.intersection(graph[v]), copy_x.intersection(graph[v]), graph)
        copy_p.remove(v)
        copy_x.add(v)

bron_kerbosch(set(), set(adjacency_dict.keys()), set(), adjacency_dict)

max_clique = set()
for clique in cliques:
    if len(clique) > len(max_clique):
        max_clique = clique
print(",".join(sorted(list(max_clique))))

        