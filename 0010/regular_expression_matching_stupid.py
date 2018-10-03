"""
Stupid solution for Regular Expression Matching.

Idea:
Matching.
"""

# Solution.
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        for i in range(len(p)):

# Main.
if __name__ == "__main__":
    s = "ab"
    p = ".*"
    solution = Solution()
    print(solution.isMatch(s, p))
