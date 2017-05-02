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
        def match(c1, c2):
            if (c1 == "(" and c2 == ")") \
               or (c1 == "{" and c2 == "}") \
               or (c1 == "[" and c2 == "]"):
                return True
            else:
                return False

        stack = []
        for c in s:
            if c in {"(", "{", "["}:
                stack.append(c)
            else:
                try:
                    if not match(stack.pop(-1), c):
                        return False
                except IndexError:
                    return False
        return len(stack) == 0

# Main.
if __name__ == "__main__":
    s = "["
    print Solution().isValid(s)
