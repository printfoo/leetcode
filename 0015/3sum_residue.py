"""
Stupid solution for 3Sum, O(n^2).

Idea:
Maintain a residue set for the last element.
Each element record what is needed in the future, so future look up, if exists then ok
"""

# Solution.
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        nums_len, res = len(nums), set()
        for i in range(nums_len - 1): # first element
            n1 = nums[i]
            if i > 0 and nums[i - 1] == n1:
                continue
            residue = set()
            for j in range(i + 1, nums_len):
                n2 = nums[j]
                if n2 not in residue:
                    residue.add(- n1 - n2)
                else:
                    res.add((n1, n2, - n1 - n2))
        return [[r[0], r[1], r[2]] for r in res]

# Main.
if __name__ == "__main__":
    nums = [0, 0, 0, 0]
    print(Solution().threeSum(nums))
