"""
Solution for Closest Binary Search Tree Value.

Idea:
DFS.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        stack = [root]
        closest_value = float("inf")
        closest_difference = float("inf")
        while stack:
            node = stack.pop()
            if not node:
                continue
            if abs(node.val - target) < closest_difference:
                closest_difference = abs(node.val - target)
                closest_value = node.val
            stack.extend([node.right, node.left])
        return closest_value

# Main.
if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    target = 3.714286
    print(Solution().closestValue(root, target))
