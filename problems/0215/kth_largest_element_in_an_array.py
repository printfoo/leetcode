"""
Solution for Kth Largest Element in an Array, Time O(n log k).

Idea:
Priority queue.
Add ID to avoid dup which is not allowed in heapq.
"""

from __future__ import annotations
import heapq

# Solution.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for n in nums:
            if len(q) < k:
                heapq.heappush(q, [n, id(n)])
            else:
                heapq.heappushpop(q, [n, id(n)])
        return q[0][0]

# Main.
if __name__ == "__main__":
    nums = [3,2,3,1,2,4,5,5,6]
    k = 4
    print(Solution().findKthLargest(nums, k))
