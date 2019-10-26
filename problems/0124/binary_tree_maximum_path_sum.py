"""
Solution for Binary Tree Maximum Path Sum.

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
    def maxPathSum(self, root: TreeNode) -> int:
        def visit_and_sum(node):
            if not node:
                return 0
            left = visit_and_sum(node.left)  # Max from left child.
            right = visit_and_sum(node.right)  # Max from right child.
            self.max_sum = max(self.max_sum, node.val, left + node.val, right + node.val, left + right + node.val)  # Global max.
            return max(node.val, left + node.val, right + node.val)  # Local max.
            
        self.max_sum = -float("inf")
        visit_and_sum(root)
        return self.max_sum

# Main.
if __name__ == "__main__":
    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().maxPathSum(root))
