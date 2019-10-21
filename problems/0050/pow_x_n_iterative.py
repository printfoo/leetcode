"""
Solution for Pow(x, n), Time O(log n), Space O(1).

Idea:
x^7:                    x x x x x x x.
(x^2)^3 * x:            x^2 x^2 x^2 | x
((x^2)^2) * x^2 * x     (x^2)^2 | x^2 | x
...
"""

# Solution
class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0: x, n = 1 / x, -n
        res = 1
        while n:
            if n % 2: res *= x
            x *= x
            n //= 2
        return res

# Main.
if __name__ == "__main__":
    x = 2
    n = -5
    print(Solution().myPow(x, n))
