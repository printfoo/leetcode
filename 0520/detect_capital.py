"""
Solution for longest uncommon subsequence, O(n).

Idea:
"""

class Solution:
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cap, low, len_word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "abcdefghijklmnopqrstuvwxyz", len(word)
        if len_word <= 1: return True
        if word[0] in cap and word[1] in cap:
            if len_word <= 2: return True
            for w in word[2:]:
                if w in low: return False
        if word[0] in cap and word[1] in low:
            if len_word <= 2: return True
            for w in word[2:]:
                if w in cap: return False
        if word[0] in low:
            for w in word[1:]:
                if w in cap: return False
        return True

# Main.
if __name__ == "__main__":
    word = "Go"
    print(Solution().detectCapitalUse(word))
