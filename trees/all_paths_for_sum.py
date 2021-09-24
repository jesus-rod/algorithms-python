# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.

# S: 12
# Output: [[1, 7, 4], [1, 9, 2]]
# Explanation: Here are the two paths with sum '12':1 -> 7 -> 4 and 1 -> 9 -> 2

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 1. Create helper taking current path [], and paths found starting as []
# 2. If root is null, end execution of current recursive call
# 3. If current node is a leaf and equals the target_sum, append current path to the paths_found
# 4. Else, call recursively on right and left children (dfs) change target sum to be target_sum - currentNode.value
# 5. After recursive calls are done, delete current node from current path to backtrack (while we are going up the recursive stack)
def find_paths(root, target_sum):
    paths_found = []
    find_paths_helper(root, target_sum, [], paths_found)
    return paths_found


def find_paths_helper(root, target_sum, current_path, paths_found):

    # Base case 1
    if root is None:
        return

    print("got called with current path",
          current_path, "we are at node", root.val)

    current_path.append(root.val)
    is_leaf = root.left is None and root.right is None
    is_target_sum = target_sum == root.val

    # Base case 2
    if is_leaf and is_target_sum:
        paths_found.append(list(current_path))
    else:
        find_paths_helper(root.left, target_sum - root.val,
                          current_path, paths_found)
        find_paths_helper(root.right, target_sum - root.val,
                          current_path, paths_found)

    del current_path[-1]


def main():

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) +
          ": " + str(find_paths(root, sum)))


main()
