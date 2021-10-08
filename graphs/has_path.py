"""
    has path
Write a function, has_path, that takes in a dictionary representing the adjacency list of a directed acyclic graph and two nodes (src, dst).
The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.
"""


def has_path(graph, src, dst):

    return dfs(graph, src, dst)


def dfs(graph, root, dst):

    if root == dst:
        return True

    for neighbour in graph[root]:
        if dfs(graph, neighbour, dst):
            return True

    return False


graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

print(has_path(graph, 'f', 'k'))  # True
