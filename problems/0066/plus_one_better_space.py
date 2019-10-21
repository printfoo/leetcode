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
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else: digits[i] = 0
        return [1] + [0] * len(digits)

# Main.
if __name__ == "__main__":
    digits = [9, 9, 9, 9]
    print(Solution().plusOne(digits))
