"""
Solution for Reverse Vowels of A String, Time O(n) Space O(1).

Idea:
Diectly reverse.
"""

# Solution
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] not in vowels:
                l += 1
                continue
            if s[r] not in vowels:
                r -= 1
                continue
            s[r], s[l] = s[l], s[r]
            l += 1
            r -= 1
        return "".join(s)

# Main.
if __name__ == "__main__":
    s = "aA"
    print(Solution().reverseVowels(s))
