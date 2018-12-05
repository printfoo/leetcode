"""
Solution for Lowest Common Ancestor of a Binary Search Tree, Time O(n), Space O(n).

Idea:
BFS.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution.
class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        queue = [root]
        while queue:
            n = queue.pop(0)
            if not n: continue
            if p.val <= n.val <= q.val or q.val <= n.val <= p.val: return n
            queue.extend([n.left, n.right])

# Main.
if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.right = TreeNode(4)
    root.left.left = TreeNode(0)
    p = root.left
    q = root.left.right
    print(Solution().lowestCommonAncestor(root, p, q).val)
