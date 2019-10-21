"""
Solution for Symmetric Tree.

Idea:
Recursive.
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
        def checkSymmetric(left, right):
            if left == None and right == None: return True
            if left == None or right == None: return False
            if left.val != right.val: return False
            checkOut = checkSymmetric(left.left, right.right)
            checkIn = checkSymmetric(left.right, right.left)
            return checkOut and checkIn
        
        if not root: return True
        return checkSymmetric(root.left, root.right)

# Main.
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    #root.left.right = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(Solution().isSymmetric(root))
