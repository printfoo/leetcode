"""
Solution for Add Strings.

Idea:
Directly add.
"""

# Solution
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2): num1, num2 = num2, num1 # num1 is the bigger one
        l1, l2, carry, numSum = len(num1), len(num2), 0, []
        for i in range(l1):
            n1 = int(num1[l1 - i - 1])
            if l2 - i - 1 < 0: n2 = 0
            else: n2 = int(num2[l2 - i - 1])
            carry, thisSum = divmod(n1 + n2 + carry, 10)
            numSum.append(str(thisSum))
        if carry == 1: numSum.append("1")
        return "".join(numSum[::-1])

# Main.
if __name__ == "__main__":
    num1 = "1"
    num2 = "9"
    print(Solution().addStrings(num1, num2))
