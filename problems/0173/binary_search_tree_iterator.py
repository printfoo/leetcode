"""
Solution for Binary Search Tree Iterator.

Idea:
Stack.
Always trace to the leftist whenever possible.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        child = node.right
        while child:
            self.stack.append(child)
            child = child.left
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.stack)

# Main.
if __name__ == "__main__":
    root = TreeNode(7)
    root.left = TreeNode(3)
    root.right = TreeNode(15)
    root.right.left = TreeNode(9)
    root.right.right = TreeNode(20)
    obj = BSTIterator(root)
    print(obj.stack[-1].val)
    print(obj.next(), obj.hasNext())
    print(obj.next(), obj.hasNext())
    print(obj.next(), obj.hasNext())
    print(obj.next(), obj.hasNext())
    print(obj.next(), obj.hasNext())
