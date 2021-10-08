def undirected_path(edges, node_A, node_B):
    adj_list = make_adjacency_list(edges)
    return has_path(adj_list, node_A, node_B, set())


def has_path(graph, src, dst, visited):

    if src in visited:
        return False
    if src == dst:
        return True

    visited.add(src)

    for neighbor in graph[src]:
        if(has_path(graph, neighbor, dst, visited)):
            return True

    return False


def make_adjacency_list(edges):
    adj_list = {}
    for edge in edges:
        a, b = edge
        if a not in adj_list:
            adj_list[a] = []
        if b not in adj_list:
            adj_list[b] = []

        adj_list[a].append(b)
        adj_list[b].append(a)
    return adj_list


edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n')
]

print(undirected_path(edges, 'j', 'm'))  # -> True

edges = [
    ('i', 'j'),
    ('k', 'i'),
    ('m', 'k'),
    ('k', 'l'),
    ('o', 'n')
]

print(undirected_path(edges, 'k', 'o'))  # -> False
