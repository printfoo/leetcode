"""
Solution for Convert a Number to Hexadecimal.

Idea:
"""

# Solution
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num += 2 ** 32
        hex_map = "0123456789abcdef"
        hex_num = ""
        while num:
            hex_num = hex_map[num % 16] + hex_num
            num //= 16
        return hex_num

# Main.
if __name__ == "__main__":
    num = -2
    print(Solution().toHex(num))
