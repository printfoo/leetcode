"""
Solution for Diameter of Binary Tree.

Idea:
Recursion.
Update find max every call.
Return deepest every call.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution.
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        def find_depth(node):
            if not node:
                return 0
            left = find_depth(node.left)
            right = find_depth(node.right)
            self.diameter = max(self.diameter, left + right)
            return max(left, right) + 1

        self.diameter = 0
        find_depth(root)
        return self.diameter

# Main.
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    #root.left.left.left = TreeNode(6)
    print(Solution().diameterOfBinaryTree(root))
