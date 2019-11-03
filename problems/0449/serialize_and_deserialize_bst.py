"""
Solution for Serialize and Deserialize BST.

Idea:
DFS.
"""

from __future__ import annotations

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution.
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
    
        :type root: TreeNode
        :rtype: str
        """
        stack = [root]
        data = []
        while stack:
            node = stack.pop()
            if node:
                stack.extend([node.right, node.left])
                data.append(str(node.val))
            else:
                data.append("")
        return "-".join(data)
    

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            if not data[self.i]:
                self.i += 1
                return None
            else:
                node = TreeNode(int(data[self.i]))
                self.i += 1
                node.left = dfs()
                node.right = dfs()
                return node
        
        data = data.split("-")
        self.i = 0
        root = dfs()
        return root

# Main.
if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    data = Codec().serialize(root)
    print(data)
    root = Codec().deserialize(data)
    data = Codec().serialize(root)
    print(data)
