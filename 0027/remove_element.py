"""
Solution for Remove Element, time O(n) space O(1).

Idea:

"""

# Solution.
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums: return 0
        j = 0
        for i in range(len(nums)):
            if nums[i] == val: continue
            else:
                nums[j] = nums[i]
                j += 1
        return j

# Main.
if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(Solution().removeElement(nums, val))
