"""
Solution for Valid Pa;indrome II, Time O(n), Space O(1).

Idea:
When meet a mismatch, check 2 potential cases. 
"""

# Solution.
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s) // 2):
            if s[i] != s[-i-1]:
                if i: return s[i: -i-1] == s[i: -i-1][::-1] or s[i+1: -i] == s[i+1: -i][::-1]
                return s[i: -i-1] == s[i: -i-1][::-1] or s[i+1: ] == s[i+1: ][::-1] # if i == 0, need to use [:] in stead of [:0]
        return True

# Main.
if __name__ == "__main__":
    s = "abca"
    print(Solution().validPalindrome(s))
