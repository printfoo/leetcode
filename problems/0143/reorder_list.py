"""
Solution for Reorder List, Time O(n), Space O(1).

Idea:
Multiple passes.
"""

from __future__ import annotations

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution.
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return
    
        # Finds the middle of the linked list.
        one_hop = head
        two_hop = head
        while two_hop and two_hop.next:
            one_hop = one_hop.next
            two_hop = two_hop.next.next
        mid = one_hop.next
        one_hop.next = None
        
        # Reverse the last half of the list.
        head2 = None
        while mid:
            temp = mid.next
            mid.next = head2
            head2 = mid
            mid = temp
        
        # Merge two lists.
        while head2:
            temp1 = head.next
            temp2 = head2.next
            head.next = head2
            head2.next = temp1
            head = temp1
            head2 = temp2

# Main.
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(6)
    print(Solution().reorderList(head))
