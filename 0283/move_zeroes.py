"""
Inplace solution for Move Zeroes, Time O(n) Space O(1).

Idea:

"""

# Solution.
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        for i in range(len(nums)):
            if nums[i] == 0: zeroes += 1
            else: nums[i], nums[i - zeroes] = nums[i - zeroes], nums[i]
        return

# Main.
if __name__ == "__main__":
    nums = [1, 0, 0, 1, 0 , 3, 5, 0, 0]
    print(Solution().moveZeroes(nums))
