"""
Solution for Merge Two Binary Trees.

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
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            t3 = TreeNode(t1.val + t2.val)
            t3.left = self.mergeTrees(t1.left, t2.left)
            t3.right = self.mergeTrees(t1.right, t2.right)
            return t3
        else:
            return t1 or t2

# Main.
if __name__ == "__main__":
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)
    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)
    print(Solution().mergeTrees(t1, t2))
