"""
Solution for Check Completeness of a Binary Tree.

Idea:
BFS.
When the first None is encountered, all remaining ones should be None.
"""

import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution.
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                return all(not node for node in queue)
            queue.extend([node.left, node.right])
        return True

# Main.
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    print(Solution().isCompleteTree(root))
