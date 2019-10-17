"""
Solution for Continuous Subarray Sum, Time O(n).

Idea:
Maintain a map of {sum_so_far % k: index}.
If a duplicated key can be found and diff(index) > 1, return True.
"""

# Solution.
class Solution:
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) < 2:
            return False

        if k == 0:
            for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1] == 0:
                    return True
            return False
            
        sum_so_far = 0
        mod_map = {sum_so_far: -1}
        for i, n in enumerate(nums):
            sum_so_far += n
            this_mod = sum_so_far % k
            if this_mod not in mod_map:
                mod_map[this_mod] = i
            elif i - mod_map[this_mod] > 1:
                return True
        return False

# Main.
if __name__ == "__main__":
    nums = [0, 0]
    k = 0
    print(Solution().checkSubarraySum(nums, k))
