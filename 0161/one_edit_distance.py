"""
Solution for One Edit Distance, Time O(n), Space O(1).

Idea:
"""

# Solution.
class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t): s, t = t, s # s for short, t for long
        l, r = 0, 0
        for i in range(len(s)):
            if s[i] != t[i]: break
            l += 1
        for i in range(len(s) - l):
            if s[-i - 1] != t[-i - 1]: break
            r += 1
        return l + 1 + r == len(t)

# Main.
if __name__ == "__main__":
    s = "aaaaaaaa"
    t = "aaaaaaaaa"
    print(Solution().isOneEditDistance(s,t))
