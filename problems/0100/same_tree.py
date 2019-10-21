"""
Solution for Same Tree.

Idea:
DFS.
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution.
class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        p_queue, q_queue = [p], [q]
        while p_queue and q_queue:
            p_node, q_node = p_queue.pop(), q_queue.pop()
            if not p_node and not q_node: continue
            if not p_node or not q_node: return False
            if p_node.val != q_node.val: return False
            p_queue.extend([p_node.left, p_node.right])
            q_queue.extend([q_node.left, q_node.right])
        if p_queue or q_queue: return False
        return True

# Main.
if __name__ == "__main__":
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.left.left = TreeNode(3)
    p.left.right = TreeNode(4)
    p.right = TreeNode(2)
    p.right.right = TreeNode(2)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.left.left = TreeNode(3)
    q.left.right = TreeNode(4)
    q.right = TreeNode(2)
    q.right.right = TreeNode(2)
    #q.right.right.right = TreeNode(2)
    print(Solution().isSameTree(p, q))
