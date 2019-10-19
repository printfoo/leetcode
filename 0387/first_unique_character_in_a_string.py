"""
Solution for First Unique Character in a String, Time O(n).

Idea:
"""

# Solution.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        unique_indexes = [s.index(l) for l in alphabets if s.count(l) == 1]
        return min(unique_indexes) if unique_indexes else -1

# Main.
if __name__ == "__main__":
    s = "loveleetcode"
    print(Solution().firstUniqChar(s))
