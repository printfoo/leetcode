"""
Solution for First Bad Version, O(log n).

Idea:
Binary search.
"""

def isBadVersion(version):
    return version > 0

# Solution.
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def binarySearch(start, end):
            mid = (start + end) // 2
            if start > end: return 0
            if not isBadVersion(mid): return binarySearch(mid + 1, end)
            if mid > 1 and isBadVersion(mid - 1): return binarySearch(start, mid - 1)
            return mid
        
        return binarySearch(1, n)


# Main.
if __name__ == "__main__":
    n = 5
    print(Solution().firstBadVersion(n))
