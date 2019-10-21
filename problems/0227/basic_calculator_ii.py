"""
Solution for Basic Calculator II, Time O(n).

Idea:
Stack.
Save +- and run */ on the fly.
"""

# Solution.
class Solution:
    def calculate(self, s: str) -> int:
        s += "+"  # Adds a operator at end, role is similar to "=".
        operator = "+"  # The first (hidden) operator is "+".
        num = ""  # Used to concate chars to num.
        i = -1
        stack = []
        while i < len(s) - 1:
            i += 1
            if s[i].isdigit():  # If a digit char, concates to num.
                num += s[i]
            elif s[i] in {"+", "-", "*", "/"}:  # If an operator is seen, update stack.
                num = int(num)  # num concating is ended, get the num.
                if operator == "+":  # Previous operator.
                    stack.append(num)
                elif operator == "-":
                    stack.append(-num)
                elif operator == "*":
                    stack[-1] *= num
                else:  # Note that "stack[-1] //= num" is wrong because -3//2=-2.
                    stack[-1] /= num
                    stack[-1] = int(stack[-1])
                operator = s[i]  # Updates operator.
                num = ""  # Prepared to concate the next num.
        return sum(stack)

# Main.
if __name__ == "__main__":
    s = "14-3/2"
    print(Solution().calculate(s))
