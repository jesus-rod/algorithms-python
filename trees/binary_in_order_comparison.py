class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def compare_trees(root_one, root_two):
    result_one = explore_inorder(root_one, [])
    result_two = explore_inorder(root_two, [])
    return result_one == result_two


def explore_inorder(root, array):

    if root is not None:
        explore_inorder(root.left, array)
        array.append(root.val)
        explore_inorder(root.right, array)

    return array


def main():

    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)

    root_two = TreeNode(3)
    root_two.left = TreeNode(1)
    root_two.right = TreeNode(6)
    root_two.right.left = TreeNode(5)
    root_two.right.right = TreeNode(7)

    print("Trees have same in-order traversal?: " +
          str(compare_trees(root, root_two)))


main()
