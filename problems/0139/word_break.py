"""
Solution for Word Break, Time O(n*w).

Idea:
Dynamic programming.
Maintain a dp array [True, False, ...]
dp[i] is if s[:i] is a valid sequence, then the final result is dp[-1].
Update dp[i] in one pass.
dp[i] is True if for a word w:
- dp[i-|w|] is True
- s[i-|w|:i] == w.
"""

from __future__ import annotations

# Solution.
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + [False] * len(s)
        for i in range(len(s) + 1):
            for w in wordDict:
                if i >= len(w) and dp[i - len(w)] and s[i - len(w):i] == w:
                    dp[i] = True
                    break
        return dp[-1]
        

# Main.
if __name__ == "__main__":
    s = "bb"
    wordDict = ["a","b","bbb","bbbb"]
    print(Solution().wordBreak(s, wordDict))
