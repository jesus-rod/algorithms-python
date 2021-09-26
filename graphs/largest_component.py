""""
Write a function, largest_component, that takes in the adjacency list of an undirected graph.
 The function should return the size of the largest connected component in the graph.

 largest_component({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 4

"""


def largest_component(graph):
    visited = set()
    largest_component = 0
    for node in graph:
        if node in visited:
            continue
        current_component_size = dfs(node, graph, visited)
        largest_component = max(largest_component, current_component_size)

    return largest_component


def dfs(currentNode, graph, visited):
    if currentNode in visited:
        return 0

    visited.add(currentNode)
    size = 1
    for neighbor in graph[currentNode]:
        size += dfs(neighbor, graph, visited)

    return size


def main():
    result = largest_component({0: [8, 1, 5],
                                1: [0],
                                5: [0, 8],
                                8: [0, 5],
                                2: [3, 4],
                                3: [2, 4],
                                4: [3, 2]})
    print(result)


main()
