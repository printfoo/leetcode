"""
Solution for Merge Sorted Array, Time O(n), Space O(1).

Idea:
From tail to head.
"""

# Solution.
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        while n > 0 and m > 0:
            if nums1[m - 1] < nums2[n - 1]:
                nums1[m + n - 1] = nums2[n - 1] # switch value
                n -= 1
            else:
                nums1[m + n - 1] = nums1[m - 1] # switch value
                m -= 1
        if m == 0: nums1[:n] = nums2[:n]
        # if the nums1 move out first, replace all leading elements with the remaining of the second list
        # if the nums2 list move out first, we already have the right answer

# Main.
if __name__ == "__main__":
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    print(Solution().merge(nums1, m, nums2, n))
