"""
Solution for Strobogrammatic Number, Time O(n), Space O(1).

Idea:
0 for 0, 1 for 1, 6 for 9, 8 for 8, 9 for 6.
"""

# Solution.
class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        strobo = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6", "2": "#", "3": "#", "4": "#", "5": "#", "7": "#"}
        return all(strobo[num[i]] == num[-i-1] for i in range(len(num) // 2 + 1))


# Main.
if __name__ == "__main__":
    num = ""
    print(Solution().isStrobogrammatic(num))
