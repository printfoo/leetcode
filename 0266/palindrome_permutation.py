"""
Solution for Palindrome Permutation, Time O(n), Space O(1).

Idea:
Count letters and odd should be <= 1.
"""

# Solution.
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count = {}
        for c in s:
            if c not in count: count[c] = 0
            count[c] += 1
        return sum([count[c] % 2 for c in count]) <= 1


# Main.
if __name__ == "__main__":
    s = "carerac"
    print(Solution().canPermutePalindrome(s))
