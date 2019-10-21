"""
Solution for Find Peak Element, Time O(n).

Idea:
"""

from __future__ import annotations

# Solution.
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.insert(0, -float("inf"))
        nums.append(-float("inf"))
        for i in range(1, len(nums) - 1):
            if nums[i-1] < nums[i] > nums[i+1]:
                return i - 1

# Main.
if __name__ == "__main__":
    nums = [1,2,3,1]
    print(Solution().findPeakElement(nums))
