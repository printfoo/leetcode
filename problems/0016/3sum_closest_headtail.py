"""
Solution for 3Sum Closest, O(n^2).

Idea:
Check from both end, head and tail. Sort first so ordered.
"""

# Solution.
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        nums_len, res, min_diff = len(nums), [], 999999999
        for i in range(nums_len - 2): # first element
            n1 = nums[i]
            l, r = i + 1, nums_len - 1 # head and tail
            while l < r:
                n2, n3 = nums[l], nums[r]
                this_diff = target - (n1 + n2 + n3) # this difference
                if this_diff > 0: l += 1
                elif this_diff < 0: r -= 1
                else: return sum([n1, n2, n3])
                if abs(this_diff) < min_diff:
                    min_diff = abs(this_diff)
                    res = [n1, n2, n3]
        return sum(res)

# Main.
if __name__ == "__main__":
    nums = [-1,0,1,1,55]
    target = 3
    print(Solution().threeSumClosest(nums, target))
