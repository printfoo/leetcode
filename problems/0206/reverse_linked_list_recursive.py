"""
Solution for Reverse Linked List.

Idea:
Recursive. Write a traverse function to replace one by one, but only return last one.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution.
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def _reverse(node, prev):
            if not node: return prev
            temp = node.next
            node.next = prev
            return _reverse(temp, node)

        return _reverse(head, None)

# Main.
if __name__ == "__main__":
    num = 14
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    node = Solution().reverseList(head)
    print(node.val)
