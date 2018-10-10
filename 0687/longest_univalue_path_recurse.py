"""
Recursion solution for Longest Univalue Path, O(n).

Idea:
Recursively visit left and right branches and record the max length.
For each branches, only need to return the longest in left/right.
For each note, concern left + right.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution.
class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def traverse(node):
            if not node: return 0
            left_len, right_len = traverse(node.left), traverse(node.right) # longest length from left and right
            left_link, right_link = 0, 0 # if think node can be linked to left or right
            if node.left and node.val == node.left.val: left_link = left_len + 1 # link left
            if node.right and node.val == node.right.val: right_link = right_len + 1 # link right
            self.max_len = max(self.max_len, left_link + right_link) # update max length (total)
            return max(left_link, right_link) # return max length of this branch (one branch only)
        self.max_len = 0
        traverse(root)
        return self.max_len

# Main.
if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(3)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.right.right = TreeNode(6)
    print(Solution().longestUnivaluePath(root))
