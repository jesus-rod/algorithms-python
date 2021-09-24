class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Do DFS on the tree
# 2. Base case 1: if root is null, return false
# 3. Base case 2: If leaf, check if value is equal to sum. If so, return True
# 4. call recursively of left and right child with updated running sum
def has_path(root, sum):

    return has_target_sum(root, sum, 0)


def has_target_sum(root, targetSum, runningSum):

    # base case 1
    if root is None:
        return False

    # base case 2
    is_leaf = root.left is None and root.right is None
    is_target_sum = runningSum + root.val == targetSum
    if is_leaf and is_target_sum:
        return True

    left_sum = has_target_sum(root.left, targetSum, runningSum + root.val)
    right_sum = has_target_sum(root.right, targetSum, runningSum + root.val)

    return left_sum or right_sum


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))


main()
