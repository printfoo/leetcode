# Min "nice" list with left and right neighbors, (left + 1) * (right + 1) nice.

from __future__ import annotations
import collections

# Solution.
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_indexes = collections.deque([-1])
        for i, n in enumerate(nums):
            if n % 2 == 1:  # Odd.
                odd_indexes.append(i)
        odd_indexes.append(i + 1)
        nice = 0
        for i in range(1, len(odd_indexes) - k):
            left = odd_indexes[i] - odd_indexes[i - 1]
            right = odd_indexes[i + k] - odd_indexes[i + k - 1]
            nice += left * right
        return nice
        
# Main.
if __name__ == "__main__":
    nums = [2,2,2,1,2,2,1,2,2,2]
    k = 2
    print(Solution().numberOfSubarrays(nums, k))
    
