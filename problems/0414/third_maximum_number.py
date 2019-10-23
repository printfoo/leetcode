"""
Solution for Third Maximum Number, Time O(n).

Idea:
"""

from __future__ import annotations

# Solution
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxes = [-float("inf"), -float("inf"), -float("inf")]
        for num in nums:
            if num > maxes[0]:
                 maxes = [num, maxes[0], maxes[1]]
            elif num > maxes[1] and num != maxes[0]:
                maxes = [maxes[0], num, maxes[1]]
            elif num > maxes[2] and num != maxes[1] and num != maxes[0]:
                maxes = [maxes[0], maxes[1], num]
        return maxes[-1] if maxes[-1] != -float("inf") else maxes[0]
    

# Main.
if __name__ == "__main__":
    nums = [1,2,2,5,3,5]
    print(Solution().thirdMax(nums))
