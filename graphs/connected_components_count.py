from collections import deque

Write a function, connected_components_count, that takes in the adjacency list of an undirected graph.
The function should return the number of connected components within the graph.

""""
connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 2
"""


def connected_components_count(graph):

    visited = set()
    bfs_count = 0

    for node in graph:
        if node in visited:
            continue

        bfs_count += performBfs(node, graph, visited)

    return bfs_count


def performBfs(current_node, graph, visited):

    queue = deque()
    queue.append(current_node)

    while queue:
        first_in_q = queue.popleft()

        if first_in_q in visited:
            continue

        visited.add(first_in_q)
        for neighbor in graph[first_in_q]:
            queue.append(neighbor)

    return 1
