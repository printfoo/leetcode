"""
Stupid solution for Valid Parentheses, O(n).

Idea:
Stack all left-side parentheses and pop when meet a right-side.
"""

# Solution.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack, parentheses = [], {"(":")", "[":"]", "{":"}"}
        for c in s:
            if c in parentheses: stack.append(c)
            else:
                if not stack or parentheses[stack.pop()] != c: return False
        return False if stack else True

# Main.
if __name__ == "__main__":
    s = "]"
    print(Solution().isValid(s))
