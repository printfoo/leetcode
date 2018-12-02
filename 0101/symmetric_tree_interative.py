"""
Solution for Symmetric Tree.

Idea:
Interative.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution.
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        q = [[root.left, root.right]]
        while q:
            left, right = q.pop(0)
            if left == None and right == None: continue
            if left == None or right == None: return False
            if left.val != right.val: return False
            q.extend([[left.left, right.right], [left.right, right.left]])
        return True

# Main.
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(Solution().isSymmetric(root))
