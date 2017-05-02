"""
Stupid solution for Two Sum, O(n^2).

Idea:
Pairwise comparison.
"""

# Solution.
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# Main.
if __name__ == "__main__":
    nums = [1, 2, 4, 5, 6]
    target = 5
    solution = Solution()
    print solution.twoSum(nums, target)
