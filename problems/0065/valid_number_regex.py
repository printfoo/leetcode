"""
Solution for Valid Number.

Idea:
Regular expression.
"""

import re

# Solution.
class Solution:
    def isNumber(self, s: str) -> bool:
        return bool(re.match(r"^[\ \t\n]*[+-]?(\.\d+|\d+\.?\d*)([eE][+-]?\d+)?[\ \t\n]*$", s))

# Main.
if __name__ == "__main__":
    s = " 1  "
    print(Solution().isNumber(s))
