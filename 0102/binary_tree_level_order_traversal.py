"""
Solution for Binary Tree Level Order Traversal.

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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        this_q, next_q, all_q = [root], [], [[root.val]]
        while True:
            while this_q:
                node = this_q.pop(0)
                if node.left: next_q.append(node.left)
                if node.right: next_q.append(node.right)
            if not next_q: break
            this_q, next_q = next_q, []
            all_q.append([n.val for n in this_q])
        return all_q


# Main.
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    #root.left.right = TreeNode(4)
    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(Solution().levelOrder(root))
