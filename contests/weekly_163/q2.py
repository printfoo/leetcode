# set.

from __future__ import annotations

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution.
class FindElements:

    def __init__(self, root: TreeNode):
        self.elements = set()
        stack = [(root, 0)]
        while stack:
            node, val = stack.pop()
            if not node:
                continue
            node.val = val
            self.elements.add(val)
            stack.append((node.left, 2 * val + 1))
            stack.append((node.right, 2 * val + 2))

    def find(self, target: int) -> bool:
        return target in self.elements
        

# Main.
if __name__ == "__main__":
    root = TreeNode(-1)
    root.right = TreeNode(-1)
    root.right.left = TreeNode(-1)
    root.right.left.left = TreeNode(-1)
    obj = FindElements(root)
    print(obj.elements)
    for target in [1,2]:
        print(target, obj.find(target))
