"""
Solution for Goat Latin, Time O(n).

Idea:
.
"""

# solution
class Solution:
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        def parse(w): return w[1:] + w[0] if w[0] not in "aeiouAEIOU" else w
        return " ".join([parse(w) + "ma" + "a" * (i + 1) for i, w in enumerate(S.split(" "))])

# Main.
if __name__ == "__main__":
    S = "I speak Goat Latin"
    print(Solution().toGoatLatin(S))
