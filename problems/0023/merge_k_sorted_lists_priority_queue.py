"""
Solution for Merge K Sorted Lists, Time O(n logk).

Idea:
Priority Queue (heap).
Queue length k, pop and insertion is O(log k).
In total n operations.
Note: Python3's implementation of heap does not allow duplicates, therefore add id(l) to heap.
"""

from __future__ import annotations
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution.
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        current = initial = ListNode(0)
        heap = []
        for l in lists:
            if l:
                heapq.heappush(heap, [l.val, id(l), l])
        while heap:
            current.next = heapq.heappop(heap)[-1]
            current = current.next
            if current.next:
                heapq.heappush(heap, [current.next.val, id(current.next), current.next])
        return initial.next


# Main.
if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)
    l3 = ListNode(2)
    l3.next = ListNode(6)
    lists = [l1, l2, l3]
    l4 = Solution().mergeKLists(lists)
    while l4:
        print(l4.val)
        l4 = l4.next
