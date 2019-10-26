"""
Solution for Convert Binary Search Tree to Sorted Doubly Linked List.

Idea:
DFS.
Better version, efficient and elegant.
"""

# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

# Solution
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        head = Node(0, None, None)
        prev = head
        stack = []
        node = root
        while stack or node:
            while node:  # First get to the leftist if node exists.
                stack.append(node)
                node = node.left
            node = stack.pop()
            prev.right = node  # Prev right link to current node.
            node.left = prev  # Current left link to prev node.
            prev = node  # Update prev node.
            node = node.right  # Update current node to its right neighbor.
        
        # All links from the first to the second to...to the last is done.
        # However the link from the last to the first is missing.
        # Now prev is the last, head.right is the first.
        prev.right = head.right  # Link the last one's right to first.
        head.right.left = prev  # Link first one's left to last.

        return head.right

# Main.
if __name__ == "__main__":
    root = Node(4, None, None)
    root.left = Node(2, None, None)
    root.left.left = Node(1, None, None)
    root.left.right = Node(3, None, None)
    root.right = Node(5, None, None)
    head = Solution().treeToDoublyList(root)
    i = 0
    while head and i < 10:
        print(head.val)
        head = head.right
        i += 1
    i = 0
    while head and i < 10:
        print(head.val)
        head = head.left
        i += 1
