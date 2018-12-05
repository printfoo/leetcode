"""
Solution for Validate Binary Search Tree.

Idea:
Keep tracking min and max of both left and right subtree and compare.
Note that 0 == False and 0 != None, therefore more identifiers need to be used, such as "Bad" or None.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution.
class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def getMinMax(n):
            if n.left: lmin, lmax = getMinMax(n.left)
            else: lmin, lmax = None, None
            if n.right: rmin, rmax = getMinMax(n.right)
            else: rmin, rmax = None, None
            if "Bad" in {lmin, lmax, rmin, rmax}: return "Bad", "Bad"
            if (lmax and lmax >= n.val) or (rmin and rmin <= n.val): return "Bad", "Bad"
            return lmin if lmin else n.val, rmax if rmax else n.val
        
        if not root: return True
        if root.left: lmin, lmax = getMinMax(root.left)
        else: lmin, lmax = None, None
        if root.right: rmin, rmax = getMinMax(root.right)
        else: rmin, rmax = None, None
        if "Bad" in {lmin, lmax, rmin, rmax}: return False
        if (lmax and lmax >= root.val) or (rmin and rmin <= root.val): return False
        return True

# Main.
if __name__ == "__main__":
    root = TreeNode(3)
    root.right = TreeNode(30)
    root.right.left = TreeNode(10)
    root.right.left.right = TreeNode(15)
    root.right.left.right.left = TreeNode(9)
    root.right.left.right.right = TreeNode(45)
    print(Solution().isValidBST(root))
