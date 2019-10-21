"""
Solution for Binary Tree Right Side View, Time O(n).

Idea:
DFS: the first seen element at depth i.
BFS: the last seen element at depth i.
"""

from __future__ import annotations

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution,
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        right_map = {}
        depth = 0
        stack = [[root, depth]]
        while stack:
            node, depth = stack.pop()
            if node:
                if depth not in right_map:
                    right_map[depth] = node.val
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return [right_map[depth] for depth in range(max(right_map) + 1)]

# Main.
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(5)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(6)
    print(Solution().rightSideView(root))
