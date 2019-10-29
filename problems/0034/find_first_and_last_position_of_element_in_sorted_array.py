"""
Solution for Find First and Last Position of Element in Sorted Array, Time O(log n).

Idea:
Binary search.
"""

from __future__ import annotations

# Solution.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        def search_first():  # Searches first position of target.
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:  # Finds target.
                    if mid == 0 or nums[mid] > nums[mid - 1]:
                        return mid  # Finds last position.
                    else:
                        right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            return -1
        
        def search_last():  # Searches last position of target.
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:  # Finds target.
                    if mid == len(nums) - 1 or nums[mid] < nums[mid + 1]:
                        return mid  # Finds last position.
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
            return -1

        return [search_first(), search_last()]
    
        

# Main.
if __name__ == "__main__":
    nums = [5,6,7,7,8,8,8,8,10,11,12,15,100,123,1324,1455,2000]
    target = 12311
    print(Solution().searchRange(nums, target))
