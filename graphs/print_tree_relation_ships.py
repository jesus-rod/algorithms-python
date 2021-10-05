"""
Input: [{animal: mammal}, {lifeform: animal}, {cat: lion}, {mammal: cat}, {animal:bird}, {animal:fish}]
Output:
    lifeform
        animal
            mammal
                cat
                    lion
        bird
        fish
"""


def print_tree_relationships(relationships):
    adjacency_list = {}
    root_candidates = {}
    for parent, child in relationships:
        if parent in adjacency_list:
            adjacency_list[parent].append(child)
        else:
            adjacency_list[parent] = [child]

        if parent not in root_candidates:
            root_candidates[parent] = True
        root_candidates[child] = False

    parent = get_parent(root_candidates)
    explore(parent, adjacency_list, 0)


def get_parent(possible_parents):
    for parent in possible_parents:
        if possible_parents[parent]:
            return parent
    return None


def explore(root, adjacency_list, tabs):

    print_with_tabs(root, tabs)
    if root not in adjacency_list:
        return
    for value in adjacency_list[root]:
        explore(value, adjacency_list, tabs + 1)


def print_with_tabs(item, tabs):
    for _ in range(tabs):
        print("     ", end="", flush=True)
    print(item)


relationships = [("animal", "mammal"), ("lifeform", "animal"),
                 ("cat", "lion"), ("mammal", "cat"), ("animal", "bird"), ("animal", "fish")]

print_tree_relationships(relationships)
