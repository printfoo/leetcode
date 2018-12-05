"""
Solution for Subarray Product Less Than K, Time O(n), Space O(1).

Idea:
Track subarray using index instead of real array.
"""

# solution
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start, count, prod = 0, 0, 1
        for i, n in enumerate(nums):
            if n >= k:
                start, prod = i, n
                continue
            while prod * n >= k:
                prod //= nums[start]
                start += 1
            prod *= n
            count += i - start + 1
        return count

# Main.
if __name__ == "__main__":
    nums = [10, 500, 2, 6]
    k = 100
    print(Solution().numSubarrayProductLessThanK(nums, k))
