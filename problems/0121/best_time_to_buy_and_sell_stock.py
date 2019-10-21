"""
Solution for Best Time to Buy and Sell Stock, Time O(n), Space O(1).

Idea:
Remember final and current.
"""

# Solution.
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        buy, sell, profit = prices[0], prices[0], 0
        for p in prices:
            if p < buy: buy = p
            if p - buy > profit: sell, profit = p, p - buy
        return profit


# Main.
if __name__ == "__main__":
    prices = [7,3,5,1,6,4]
    print(Solution().maxProfit(prices))
