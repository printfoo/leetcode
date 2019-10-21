"""
Solution for Plus one.

Idea:
Plus one and carry
"""

# solution
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        output, carry = [], 1
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + carry < 10:
                output.append(digits[i] + carry)
                carry = 0
            else:
                output.append(0)
                carry = 1
        if carry == 1: output.append(1)
        output.reverse()
        return output

# Main.
if __name__ == "__main__":
    digits = [8, 8, 7, 8]
    print(Solution().plusOne(digits))
