"""
Solution for Best Time to Buy and Sell Stock II, Time O(n), Space O(1).

Idea:
First note: profit = sum(peak-valley) = sum(peak)-sum(valley)
Second note: profit = sum( if n[i] < n[i+1] )
"""

from __future__ import annotations

# Solution.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(max(0, prices[i+1] - prices[i]) for i in range(len(prices) - 1))


# Main.
if __name__ == "__main__":
    prices = [7,3,5,1,6,4]
    print(Solution().maxProfit(prices))
