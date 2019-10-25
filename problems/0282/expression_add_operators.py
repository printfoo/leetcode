"""
Solution for Expression Add Operators.

Idea:
- DFS.
- Recurse through all possibilities.
- Save value on the fly.
- Remember prev to deal with *.
"""

from __future__ import annotations

# Solution.
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        def dfs(index, expression, val, prev_val):
            if index == len(num) and val == target:  # Reaches the end and target value.
                self.ans.append(expression)  # Adds an expression.
                return  # Done this round.

            for next_index in range(index + 1, len(num) + 1):  # Traverse all number possibilities, ie, NO-OP.
                if next_index == index + 1 or num[index] != "0":  # Corner case: +05, *004, etc is not allowed, but just 0 is okay.
                    next_val = int(num[index: next_index])  # Value of possible NO-OP.
                    if prev_val == "beginning":  # Corner case: the begining of the recursion.
                        dfs(next_index, num[index: next_index],
                            next_val, next_val)  # No op in the beginning.
                    else:
                        dfs(next_index, expression+"+"+num[index: next_index],
                            val+next_val, next_val)  # +
                        dfs(next_index, expression+"-"+num[index: next_index],
                            val-next_val, -next_val)  # -
                        dfs(next_index, expression+"*"+num[index: next_index],
                            val-prev_val+prev_val*next_val, prev_val*next_val)  # *, cancel previous
    
        self.ans = []
        dfs(0, "", 0, "beginning")
        return self.ans

# Main.
if __name__ == "__main__":
    num = "34562374904"
    target = 9193
    print(Solution().addOperators(num, target))
