"""
Clever solution for Reverse Interger, O(n).

Idea:
Use the number itself.
"""

# Solution.
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0

        sign = 1 if x > 0 else -1
        x = x * sign

        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x = x / 10

        y = y * sign
        if y > 2 ** 31 - 1 or y < -2 ** 31:
            return 0
        return y

# Main.
if __name__ == "__main__":
    x = 0
    solution = Solution()
    print solution.reverse(x)
