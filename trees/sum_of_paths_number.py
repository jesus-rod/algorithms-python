# Given a binary tree where each node can only have a digit (0-9) value,
# each root-to-leaf path will represent a number. Find the total sum of all the numbers represented by all paths.

# Output: 332 Explanation: The sum of all path numbers: 101 + 116 + 115


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_sum_of_path_numbers(root):
    return find_sum_of_path_numbers_helper(root, 0)


def find_sum_of_path_numbers_helper(currentNode, runningSum):

    # Base case 1
    if currentNode is None:
        return 0

    updatedSum = 10 * runningSum + currentNode.val

    # Base case 2
    is_leaf = currentNode.left is None and currentNode.right is None
    if is_leaf:
        return updatedSum

    left_sum = find_sum_of_path_numbers_helper(currentNode.left, updatedSum)
    right_sum = find_sum_of_path_numbers_helper(currentNode.right, updatedSum)

    return left_sum + right_sum


def main():
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
