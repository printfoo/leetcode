"""
Solution for Longest Valid Parentheses, Time O(n), Space O(1).

Idea:
Traverse twice, left->right and right->left
"""

# Solution.
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        left, right = 0, 0
        for c in s:
            if c == ")": right += 1
            if c == "(": left += 1
            if right > left: left, right = 0, 0
            elif right == left: longest = max(longest, right + left)
        left, right = 0, 0
        for c in s[::-1]:
            if c == ")": right += 1
            if c == "(": left += 1
            if left > right: left, right = 0, 0
            elif right == left: longest = max(longest, right + left)
        return longest

# Main.
if __name__ == "__main__":
    s = "()"
    print(Solution().longestValidParentheses(s))
