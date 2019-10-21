"""
Solution for Minimum Genetic Mutation.

Idea:

"""

# Solution
class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        m = 1
        while n >= m:
            n -= m
            m += 1
        return m - 1

# Main.
if __name__ == "__main__":
    n = 3
    print(Solution().arrangeCoins(n))
