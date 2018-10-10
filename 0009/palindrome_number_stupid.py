"""
Stupid solution for Palindrome Number, O(n).

Idea:
Reverse and compare.
"""

# Solution.
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        xc = x
        if x < 0:
            return False

        y = 0
        while x > 0:
            y = y * 10 + x % 10
            x = x / 10

        return y == xc

# Main.
if __name__ == "__main__":
    x = 0
    print(Solution().isPalindrome(x))
