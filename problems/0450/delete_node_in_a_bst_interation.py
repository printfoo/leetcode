"""
Solution for Delete Node in a BST, Average time O(log n), worse O(n), Space O(1).

Idea:
Interation.
"""

from __future__ import annotations

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution.
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def replace(node):
            if not node.left and not node.right:  # If this node has no child.
                return None
            elif not node.left:  # If this node has no left child.
                return node.right  # Return its right child to connect.
            elif not node.right:  # If this node has no right child.
                return node.left  # Return its left child to connect.
            else:  # If this node has both left and right child.
                to_return = node.right  # Return its right child
                to_connect = node.left  # Try to find a place to connect left child.
                node = to_return
                while node.left:  # From right, continue to find an open left slot.
                    node = node.left
                node.left = to_connect  # Connect that left slot to connect.
                return to_return
        
        if not root:
            return root
        elif root.val == key:
            return replace(root)
        node = root
        while node:
            if node.left and node.left.val == key:
                node.left = replace(node.left)
                break
            elif node.right and node.right.val == key:
                node.right = replace(node.right)
                break
            elif node.val > key:
                node = node.left
            elif node.val < key:
                node = node.right
        return root

# Main.
if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    key = 3
    root = Solution().deleteNode(root, key)
    print(root.left.left.val)
