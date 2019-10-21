"""
Solution for Minimum Depth of Binary Tree.

Idea:
Recursion.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution.
class Solution:
    def minDepth(self, root: TreeNode) -> int:

        def depth(node):
            if not node.left and not node.right:
                return 1
            left = depth(node.left) if node.left else float("inf")
            right = depth(node.right) if node.right else float("inf")
            return min(left, right) + 1
            
        if not root:
            return 0
        return depth(root)
        

# Main.
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    print(Solution().minDepth(root))
