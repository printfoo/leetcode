"""
Solution for Majority Element, Time O(n).

Idea:
"""

from __future__ import annotations

# Solution.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 0
            counter[num] += 1
            if counter[num] * 2 > len(nums):
                return num
        return None

# Main.
if __name__ == "__main__":
    nums = [2,2,1,1,1,2,2]
    print(Solution().majorityElement(nums))
