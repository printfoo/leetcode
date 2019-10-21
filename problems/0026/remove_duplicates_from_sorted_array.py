"""
Solution for Remove Duplicates from Sorted Array, time O(n) space O(1).

Idea:

"""

# Solution.
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == nums[j]: continue
            else:
                j += 1
                nums[j] = nums[i]
        return j + 1

# Main.
if __name__ == "__main__":
    nums = [1]
    print(Solution().removeDuplicates(nums))
