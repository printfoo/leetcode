"""
Dynamic Programming Solution for House Robber, Time O(n), Space O(1).

Idea:
f(0) = n[0]
f(1) = max(n[0], n[1])
f(x) = max(f(x-2), f(x-1) + n[x])
"""

# Solution
class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fx_2, fx_1 = 0, 0
        for n in nums: fx_2, fx_1 = fx_1, max(fx_2 + n, fx_1)
        return fx_1

# Main.
if __name__ == "__main__":
    nums = [1,2,3,1]
    print(Solution().rob(nums))
