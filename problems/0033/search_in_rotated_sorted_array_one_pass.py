"""
Solution for Search in Rotated Sorted Array, Time O(log n).

Idea:
Binary search and one pass.
Better understandable by drawing.
"""

from __future__ import annotations

# Solution.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[right]:  # Pivot is in mid-right.
                if nums[left] <= target < nums[mid]:  # Target in left-mid.
                    right = mid - 1  # Search left.
                else:
                    left = mid + 1  # Search right.
            else:  # pivot is in left-mid
                if nums[mid] < target <= nums[right]:  # Target in mid-right.
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
        

# Main.
if __name__ == "__main__":
    nums = [1]
    target = 2
    print(Solution().search(nums, target))
