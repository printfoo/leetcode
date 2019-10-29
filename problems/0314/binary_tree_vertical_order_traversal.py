"""
Solution for Binary Tree Vertical Order Traversal. Time O(nlogn)

Idea:
DFS and record locations.
Sort locations and output.
Similar to 987, except small ordering difference.
"""

from __future__ import annotations

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# solution
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        vertical_record = {}
        stack = [[root, 0, 0]]
        while stack:
            node, x, y = stack.pop()
            if node:
                if x not in vertical_record:
                    vertical_record[x] = {}
                if y not in vertical_record[x]:
                    vertical_record[x][y] = []
                vertical_record[x][y].append(node.val)
                stack.append([node.right, x+1, y+1])
                stack.append([node.left, x-1, y+1])
        ans = []
        xs = list(vertical_record.keys())
        xs.sort()
        for x in xs:
            ys = list(vertical_record[x].keys())
            ys.sort()
            ans.append([])
            for y in ys:
                elements = vertical_record[x][y]
                ans[-1].extend(elements)
        return ans

# Main.
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(7)
    print(Solution().verticalOrder(root))
