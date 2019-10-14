"""
Solution for Find Peak Element, Time O(log n).

Idea:
Binary search.
Start from middle index i:
If nums[i-1] > nums[i] > nums[i+1]: peak on the left.
If nums[i-1] < nums[i] < nums[i+1]: peak on the right.
If nums[i-1] < nums[i] > nums[i+1]: i is the peak.
If nums[i-1] > nums[i] < nums[i+1]: peaks on both left and right.
"""

from __future__ import annotations

# Solution.
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def binary_search_peak(left, right):
            if right - left <= 1:
                return left if max(nums[left], nums[right]) == nums[left] else right
            mid = (left + right) // 2
            if nums[mid-1] < nums[mid] > nums[mid+1]:
                i = mid
            elif nums[mid-1] > nums[mid] > nums[mid+1]:
                i = binary_search_peak(left, mid)
            else:
                i = binary_search_peak(mid, right)
            return i

        nums.insert(0, -float("inf"))
        nums.append(-float("inf"))
        i = binary_search_peak(1, len(nums) - 2)
        return i - 1

# Main.
if __name__ == "__main__":
    nums = [1,2]
    print(Solution().findPeakElement(nums))
