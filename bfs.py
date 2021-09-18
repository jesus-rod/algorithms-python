from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = []

    if root is None:
        return result

    queue = deque()
    queue.append(root)

    while queue:
        currentLevel = []
        levelSize = len(queue)
        for _ in range(levelSize):
            queueItem = queue.popleft()
            currentLevel.append(queueItem.val)

            if queueItem.left:
                queue.append(queueItem.left)
            if queueItem.right:
                queue.append(queueItem.right)

        result.append(currentLevel)

    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
