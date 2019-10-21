"""
Solution for Reverse Linked List.

Idea:
Iterative. Temporary store next one.
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
        previous = None
        while head:
            temp = head.next
            head.next = previous
            previous = head
            head = temp
        return previous

# Main.
if __name__ == "__main__":
    num = 14
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    node = Solution().reverseList(head)
    print(node.val, node.next.val)
