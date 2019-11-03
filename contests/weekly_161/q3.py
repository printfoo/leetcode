# Two pass: left to right and right to left.

from __future__ import annotations
import collections

# Solution.
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        parentheses_count = {"(": 0, ")": 0}
        left_s = ""
        for c in s:
            if c not in parentheses_count:
                left_s += c
            elif c == "(":
                parentheses_count["("] += 1
                left_s += c
            elif c == ")" and parentheses_count["("] > 0:
                parentheses_count["("] -= 1
                left_s += c
        right_c = ""
        for c in left_s[::-1]:
            if c == "(" and parentheses_count["("] > 0:
                parentheses_count["("] -= 1
                continue
            right_c += c
        return right_c[::-1]

# Main.
if __name__ == "__main__":
    s = "(a(b(c)d)"
    print(Solution().minRemoveToMakeValid(s))
