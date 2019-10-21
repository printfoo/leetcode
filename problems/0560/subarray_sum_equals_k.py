"""
Solution for Subarray Sum Equals K, O(n).

Idea:
K = sum(nums[i:j]) = sum(nums[:j]) - sum(nums[:i])
"""

from collections import Counter

# Solution.
class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_counter = Counter()
        sum_so_far = 0
        sum_counter[sum_so_far] += 1
        sum_to_k = 0
        for n in nums:
            sum_so_far += n
            sum_to_k += sum_counter[sum_so_far - k]
            sum_counter[sum_so_far] += 1
        return sum_to_k

# Main.
if __name__ == "__main__":
    nums = [1]
    k = 0
    print(Solution().subarraySum(nums, k))
