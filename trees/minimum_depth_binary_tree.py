from collections import deque
import math

# 1. Do a DFS
# 2. Have two vars for tracking minDepth and runningDepth
# 3. On each DFS running level, add one to runningDepth
# 4. When checking for each node, check if it's a leaf
# 5. If it's a leaf, check if minDepth = (minDepth, runningDepth)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_minimum_depth(root):

    if root is None:
        return 0

    queue = deque()
    queue.append(root)

    minDepth = math.inf
    runningDepth = 0
    levelSize = len(queue)
    while queue:
        levelSize = len(queue)
        runningDepth += 1

        for _ in range(levelSize):
            qItem = queue.popleft()

            if qItem.left:
                queue.append(qItem.left)
            if qItem.right:
                queue.append(qItem.right)

            isLeaf = qItem.right is None and qItem.left is None
            if isLeaf:
                minDepth = min(minDepth, runningDepth)

    return minDepth


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()
