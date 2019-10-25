"""
Solution for Valid Number.

Idea:
"""

# Solution.
class Solution:
    def isNumber(self, s: str) -> bool:
        signs = "+-"
        digits = "0123456789"
        s = s.strip().lower()  # allow leading and trailing space, \t, and \n
        if not s:
            return False
        
        # After e can only be +-int.
        exp_split = s.split("e")
        if len(exp_split) > 2:
            return False
        after_e = None
        if len(exp_split) > 1:
            after_e = exp_split[1]
            if after_e == "":
                return False
            if after_e[0] in signs:
                after_e = after_e[1:]
        before_e = exp_split[0]
        if after_e == "" or before_e in {"", "+", "-"}:
            return False

        # After dot can only be int, before dot can only be +-int.
        dot_split = before_e.split(".")
        if len(dot_split) > 2:
            return False
        before_dot = dot_split[0]
        if before_dot != "" and before_dot[0] in signs:
             before_dot = before_dot[1:]
        after_dot = None
        if len(dot_split) > 1:
            after_dot = dot_split[1]
        if before_dot == "" and after_dot == "":
            return False

        # Now three parts should all be int.
        for pmint in [before_dot, after_dot, after_e]:
            if pmint:
                for c in pmint:
                    if c not in digits:
                        return False
    
        return True

# Main.
if __name__ == "__main__":
    s = "+.8"
    print(Solution().isNumber(s))
