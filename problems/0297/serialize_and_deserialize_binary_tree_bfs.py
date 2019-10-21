"""
Solution for Serialize and Deserialize Binary Tree.

Idea:
BFS.
Note: Python List[] can be used as stack by pop().
It can also be used as queue by pop(0) but very slow.
A better solution is to use collections.deque(List[]) and popleft().
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
        data = []
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                data.append(str(node.val))
                queue.extend([node.left, node.right])
            else:
                data.append('')
        return ','.join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
            
        :type data: str
        :rtype: TreeNode
        """
        data = collections.deque(data.split(','))
        val_root = data.popleft()
        if not val_root:
            return None
        root = TreeNode(int(val_root))
        queue = collections.deque([root])
        while data:
            node = queue.popleft()
            val_left = data.popleft()
            val_right = data.popleft()
            if val_left:
                node.left = TreeNode(int(val_left))
                queue.append(node.left)
            if val_right:
                node.right = TreeNode(int(val_right))
                queue.append(node.right)
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
