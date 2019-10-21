"""
Solution for Single Number, Time O(n) Space O(1).

Idea:
Bit manipulation: a^0=a, a^a=0, a^b^a^b^c=c
"""

# Solution.
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single = 0
        for n in nums:
            single ^= n
        return single

# Main.
if __name__ == "__main__":
    nums = [4,1,2,1,2]
    print(Solution().singleNumber(nums))
