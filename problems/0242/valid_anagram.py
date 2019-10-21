"""
Solution for Valid Anagram, Time O(n), Space O(1).

Idea:
Dict.
"""

# Solution.
class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sd, td = {}, {}
        for c in "abcdefghijklmnopqrstuvwxyz": sd[c], td[c] = 0, 0
        for c in s: sd[c] += 1
        for c in t: td[c] += 1
        return sd == td

# Main.
if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))
