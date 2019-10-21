"""
Stupid solution for Add Two Numbers, O(n).

Idea:
Traverse linked lists.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution.
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        x = l1
        y = l2
        carry = 0
        start = ListNode(0)
        point = start
        while True:
            s = ListNode(int(x.val + y.val + carry) % 10)
            carry = int(x.val + y.val + carry) / 10
            point.next = s
            point = s
            x = x.next
            y = y.next
            if x == None and y != None:
                x = ListNode(0)
            if x != None and y == None:
                y = ListNode(0)
            if x == None and y == None:
                if carry > 0:
                    s = ListNode(carry)
                    point.next = s
                break
        return start.next

# Main.
if __name__ == "__main__":
    """
    x1 = ListNode(2)
    x2 = ListNode(4)
    x3 = ListNode(3)
    x4 = ListNode(1)
    x1.next = x2
    x2.next = x3
    x3.next = x4

    y1 = ListNode(5)
    y2 = ListNode(6)
    y3 = ListNode(4)
    y1.next = y2
    y2.next = y3
    """
    x1 = ListNode(5)
    y1 = ListNode(5)

    solution = Solution()
    p = solution.addTwoNumbers(x1, y1)
    while True:
        print(p.val),
        p = p.next
        if p == None:
            break
