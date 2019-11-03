# GCD of all elements should be 1.

from __future__ import annotations
import math

# Solution.
class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        gcd = nums[0]
        for n in nums:
            gcd = math.gcd(gcd, n)
        return gcd == 1

# Main.
if __name__ == "__main__":
    nums = [6, 10, 15]
    print(Solution().isGoodArray(nums))
