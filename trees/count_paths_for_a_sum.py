# Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’.
# Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).

# S: 11
# Output: 2
# Explanation: Here are the two paths with sum '11':7 -> 4 . and 1 -> 10.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_paths(root, S):
    paths_found = []
    count_paths_helper(root, S, [], paths_found)
    print(paths_found)
    return len(paths_found)


def count_paths_helper(current_node, target_sum, current_path, paths_found):
    if current_node is None:
        return

    current_path.append(current_node.val)

    is_target_sum = target_sum == current_node.val

    if is_target_sum:
        paths_found.append(list(current_path))

    count_paths_helper(current_node.left, target_sum -
                       current_node.val, current_path, paths_found)

    count_paths_helper(current_node.right, target_sum -
                       current_node.val, current_path, paths_found)

    count_paths_helper(current_node.left, target_sum, [], paths_found)

    count_paths_helper(current_node.right, target_sum, [], paths_found)


def main():
    root = TreeNode(11)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))


main()
