"""
Solution for Range Sum of BST, Time O(n).

Idea:
DFS.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution.
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    sum += node.val
                if node.val >= L:
                    stack.append(node.left)
                if node.val <= R:
                    stack.append(node.right)
        return sum

# Main.
if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    L = 7
    R = 15
    print(Solution().rangeSumBST(root, L, R))
