class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(3)
root.right.right.right = TreeNode(3)

print("maxDepth is ", maxDepth(root))