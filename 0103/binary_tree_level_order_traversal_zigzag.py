"""
Solution for Binary Tree Level Order Traversal Zigzag.

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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        this_q, next_q, all_q = [root], [], [[root.val]]
        zigzag = True
        while True:
            while this_q:
                node = this_q.pop(0)
                if node.left: next_q.append(node.left)
                if node.right: next_q.append(node.right)
            if not next_q: break
            this_q, next_q = next_q, []
            vals = [n.val for n in this_q]
            if zigzag: all_q.append(vals[::-1])
            else: all_q.append(vals)
            zigzag = not zigzag
        return all_q


# Main.
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    #root.left.left = TreeNode(3)
    #root.left.right = TreeNode(4)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().zigzagLevelOrder(root))
