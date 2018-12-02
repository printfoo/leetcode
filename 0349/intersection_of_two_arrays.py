"""
Solution for intersection of two arrays, Time O(n).

Idea:
Easy.
"""

# Solution
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter, nums1, nums2 = [], {n for n in nums1}, {n for n in nums2}
        for n in nums1:
            if n in nums2 and n not in inter: inter.append(n)
        return inter

# Main.
if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(Solution().intersection(nums1, nums2))
