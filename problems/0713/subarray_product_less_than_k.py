"""
Solution for Subarray Product Less Than K, Time O(n), Space O(n).

Idea:
Sliding window.
"""

# solution
class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        subarray, count, prod = [], 0, 1
        for n in nums:
            if n >= k:
                subarray, prod = [], 1
                continue
            while prod * n >= k: prod //= subarray.pop(0)
            prod *= n
            subarray.append(n)
            count += len(subarray)
        return count

# Main.
if __name__ == "__main__":
    nums = [10, 500, 2, 6]
    k = 100
    print(Solution().numSubarrayProductLessThanK(nums, k))
