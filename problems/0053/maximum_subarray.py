"""
Solution for Maximum Subarray, Time O(n), Space O(1).

Idea:
Pick the locally optimal move at each step, and that will lead to the globally optimal solution.
"""

# Solution.
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_max = -float("inf")
        global_max = -float("inf")
        for n in nums:
            local_max = max(local_max + n, n)
            global_max = max(global_max, local_max)
        return global_max

# Main.
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().maxSubArray(nums))
