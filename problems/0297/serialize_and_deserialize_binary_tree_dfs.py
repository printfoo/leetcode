"""
Solution for Serialize and Deserialize Binary Tree.

Idea:
DFS.
"""

import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
            
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                data.append('')
            else:
                data.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        data = []
        dfs(root)
        return ','.join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
            
        :type data: str
        :rtype: TreeNode
        """
        def dfs():
            if not data[index[0]]:
                index[0] += 1
                return None
            else:
                node = TreeNode(int(data[index[0]]))
                index[0] += 1
                node.left = dfs()
                node.right = dfs()
                return node
        data = data.split(',')
        index = [0]  # has to be a list here other wise index cannot be global to dfs()
        root = dfs()
        return root

if __name__ == "__main__":
    root = TreeNode(1)
    #root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    codec = Codec()
    print(codec.serialize(root))
    print(codec.serialize(codec.deserialize(codec.serialize(root))))
