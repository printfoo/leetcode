"""
Solution for Longest Continuous Increasing Subsequence, Time O(n), Space O(1).

Idea:
Remember location.
"""
from typing import List

# Solution.
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        LCIS, thisCIS = 0, 1
        if not nums: return LCIS
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]: thisCIS += 1
            else: LCIS, thisCIS = max(LCIS, thisCIS), 1
        return max(LCIS, thisCIS)

# Main.
if __name__ == "__main__":
    nums = [2,1,2,3,4,5,1,2,3,1,2,3,4,5,6,7]
    print(Solution().findLengthOfLCIS(nums))
