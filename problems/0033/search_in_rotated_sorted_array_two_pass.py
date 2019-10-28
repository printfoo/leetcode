"""
Solution for Search in Rotated Sorted Array, Time O(log n).

Idea:
Two pass.
First find pivot.
And then compare target and pivot and find which part of the array to look for.
"""

from __future__ import annotations

# Solution.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            return 0 if target in nums else -1

        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] > nums[left + 1]:
                pivot = left + 1
                break
            pivot = (left + right) // 2
            if nums[pivot] > nums[right]:
                left = pivot
            elif nums[pivot] < nums[right]:
                right = pivot

        if target == nums[pivot]:
            return pivot
        elif target <= nums[-1]:
            left = pivot
            right = len(nums) - 1
        elif target >= nums[0]:
            left = 0
            right = pivot - 1
        while left <= right:
            index = (left + right) // 2
            if nums[index] < target:
                left = index + 1
            elif nums[index] > target:
                right = index - 1
            else:
                return index
        return -1
        

# Main.
if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(Solution().search(nums, target))
