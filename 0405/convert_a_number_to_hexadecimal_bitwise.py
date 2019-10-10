"""
Solution for Convert a Number to Hexadecimal.

Idea:
Bitwise operation, faster.
"""

# Solution
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        hex_map = "0123456789abcdef"
        hex_num = ""
        for i in range(8):  # works for negative as well
            hex_num = hex_map[num & 15] + hex_num  # &1111
            num >>= 4  # //=16 if positive
        return hex_num.lstrip("0")

# Main.
if __name__ == "__main__":
    num = -213421
    print(Solution().toHex(num))
