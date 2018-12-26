"""
Solution for Maximum Product Subarray.

Idea:
The problem is consecutive negative numbers.
Therefore we keep tracking max and min (negative with max abs).
"""

# Solution.
class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        local_min, local_max, global_max = 1, 1, nums[0]
        for n in nums:
            temp1, temp2 = n * local_min, n * local_max
            local_min, local_max = min(n, temp1, temp2), max(n, temp1, temp2)
            global_max = max(global_max, local_max)
        return global_max

# Main.
if __name__ == "__main__":
    nums = [-2,0,-1]
    print(Solution().maxProduct(nums))
