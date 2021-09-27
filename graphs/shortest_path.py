from collections import deque


def shortest_path(edges, node_A, node_B):
    graph = make_adjacency_list(edges)

    bfs_q = deque()
    bfs_q.append((node_A, 0))

    visited = set()

    while bfs_q:
        top_item, level = bfs_q.popleft()

        if top_item == node_B:
            return level
        if top_item in visited:
            continue

        visited.add(top_item)

        for neighbor in graph[top_item]:
            bfs_q.append((neighbor, level+1))

    return -1


def make_adjacency_list(edges):
    adjacency_list = {}
    for a, b in edges:
        if a not in adjacency_list:
            adjacency_list[a] = []
        if b not in adjacency_list:
            adjacency_list[b] = []

        adjacency_list[a].append(b)
        adjacency_list[b].append(a)
    return adjacency_list
