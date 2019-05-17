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
        return list(set(nums1) & set(nums2))

# Main.
if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(Solution().intersection(nums1, nums2))
