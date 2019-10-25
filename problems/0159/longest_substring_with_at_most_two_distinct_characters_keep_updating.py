"""
Solution for Longest Substring with At Most Two Distinct Characters, Time O(n), Space O(1).

Idea:
Similar to 904.
Keep a window of size 2 and keep updates at each step.
(This solution may be hard to understand.)
"""

# Solution.
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: "str") -> "int":
        start, end, change, max_len, cs = 0, 0, 0, 0, [None, None]
        for c in s:
            if c not in cs:
                max_len = max(max_len, end - start)
                start = change
            if c != cs[1]:
                change = end
                cs = [cs[1], c]
            end += 1
        return max(max_len, end - start)

# Main.
if __name__ == "__main__":
    s = "abaccc"
    print(Solution().lengthOfLongestSubstringTwoDistinct(s))
