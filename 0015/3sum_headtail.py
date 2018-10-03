"""
Stupid solution for 3Sum, O(n^2).

Idea:
Check from both end, head and tail. Sort first so ordered.
"""

# Solution.
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        nums_len, res = len(nums), []
        for i in range(nums_len - 2): # first element
            n1 = nums[i]
            if i > 0 and nums[i - 1] == n1: continue # duplicate first element
            if nums[i] > 0: break # already visited
            l, r = i + 1, nums_len - 1 # head and tail
            while l < r:
                n2 = nums[l]
                if l > i + 1 and nums[l - 1] == n2: # duplicate second element
                    l += 1
                    continue
                n3 = nums[r]
                if r < nums_len - 1 and nums[r + 1] == n3:  # duplicate third element
                    r -= 1
                    continue
                sum = n1 + n2 + n3 # sum
                if sum < 0: l += 1
                elif sum > 0: r -= 1
                else:
                    res.append([n1, n2, n3])
                    l += 1
                    r -= 1
        return res

# Main.
if __name__ == "__main__":
    nums = [0, 0, 0, 0, 0]
    print(Solution().threeSum(nums))
