from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = deque()

    queue = deque()
    queue.append(root)
    while queue:
        currentLevel = []
        levelSize = len(queue)
        for _ in range(levelSize):
            qItem = queue.popleft()
            currentLevel.append(qItem.val)

            if qItem.left:
                queue.append(qItem.left)
            if qItem.right:
                queue.append(qItem.right)

        result.appendleft(currentLevel)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
