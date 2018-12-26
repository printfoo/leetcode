"""
Solution for Pow(x, n), Time O(log n), Space O(log n).

Idea:
Double everytime.
"""

# Solution
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        if n < 0: return 1 / self.myPow(x, -n)
        if n % 2: return x * self.myPow(x, n - 1)
        return self.myPow(x * x, n // 2)

# Main.
if __name__ == "__main__":
    x = 2
    n = -5
    print(Solution().myPow(x, n))
