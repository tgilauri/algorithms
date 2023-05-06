def make_graph(edges):
    graph = {}
    for u, v in edges:
        graph.setdefault(u, [])
        graph[u].append(v)
    return graph


edges = [[1, 2], [3, 2], [4, 1]]
print(make_graph(edges))
