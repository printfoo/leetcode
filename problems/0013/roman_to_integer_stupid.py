"""
Stupid solution for Roman to Integer, O(n).

Idea:
Traverse.
"""

# Solution.
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        prev = 0
        length = len(s)
        for i in range(length):
            this = map[s[i]]
            if this <= prev:
                num += prev
            else:
                num -= prev
            prev = this
        num += this
        return num

# Main.
if __name__ == "__main__":
    s = "MCMXCIV"
    solution = Solution()
    print(solution.romanToInt(s))
