"""
Solution for Valid Palindrome, Time O(n), Space O(1).

Idea:
One pass
"""

# Solution.
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum(): l += 1
            while l < r and not s[r].isalnum(): r -= 1
            if s[l].lower() != s[r].lower(): return False
            l += 1
            r -= 1
        return True

# Main.
if __name__ == "__main__":
    s = "0P"
    print(Solution().isPalindrome(s))
