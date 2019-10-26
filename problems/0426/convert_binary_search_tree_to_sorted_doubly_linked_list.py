"""
Solution for Convert Binary Search Tree to Sorted Doubly Linked List.

Idea:
DFS.
My version, works, efficient but not elegant.
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

        stack = []
        while root:
            stack.append(root)
            root = root.left
            if not root:
                head = stack[-1]
                break

        prev = head
        while stack:
            node = stack.pop()
            if node.right:
                node_to_visit = node.right
                stack.append(node_to_visit)
                while node_to_visit.left:
                    node_to_visit = node_to_visit.left
                    stack.append(node_to_visit)
            if stack:
                node.right = stack[-1]
            else:
                node.right = head
                head.left = node
            node.left = prev
            prev = node

        return head

# Main.
if __name__ == "__main__":
    #root = Node(1, None, None)
    root = Node(4, None, None)
    root.left = Node(2, None, None)
    root.left.left = Node(1, None, None)
    root.left.right = Node(3, None, None)
    root.right = Node(5, None, None)
    head = Solution().treeToDoublyList(root)
    i = 0
    while head and i < 10:
        print(head.val)
        head = head.left
        i += 1
    print(head.val, head.left.val)
