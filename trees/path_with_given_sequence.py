# Path With Given Sequence (medium)
# Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
# Sequence: [1, 0, 7] Output: false Explanation: The tree does not have a path 1 -> 0 -> 7.
# Sequence: [1, 1, 6] Output: true Explanation: The tree has a path 1 -> 1 -> 6.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_path(root, sequence):
    return find_path_helper(root, sequence, [])


def find_path_helper(current_node, target_sequence, current_path):

    if current_node is None:
        return False

    current_path.append(current_node.val)

    is_leaf = current_node.left is None and current_node.right is None
    if is_leaf and current_path == target_sequence:
        return True

    left_path = find_path_helper(
        current_node.left, target_sequence, current_path)
    right_path = find_path_helper(
        current_node.right, target_sequence, current_path)

    del current_path[-1]

    return left_path or right_path


def main():

    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
