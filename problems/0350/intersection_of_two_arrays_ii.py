"""
Solution for Intersection of Two Arrays II, Time O(n).

Idea:
Hashmap.
"""
from typing import List

# Solution
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1map, numIntersec = {}, []
        for n1 in nums1:
            if n1 not in n1map: n1map[n1] = 1
            else: n1map[n1] += 1
        for n2 in nums2:
            if n2 not in n1map or n1map[n2] == 0: continue
            numIntersec.append(n2)
            n1map[n2] -= 1
        return numIntersec


# Main.
if __name__ == "__main__":
    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(Solution().intersect(nums1, nums2))
