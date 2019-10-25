"""
Solution for Longest Substring with At Most K Distinct Characters, O(kn).

Idea:
Using a dict, similar to 159.
NOT OPTIMAL.
"""

# Solution.
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_len = 0
        k_distinct = {}
        left = -1
        for right in range(len(s)):
            k_distinct[s[right]] = right
            if len(k_distinct) == k + 1:  # Too many.
                index_to_remove = min(k_distinct.values())
                left = k_distinct.pop(s[index_to_remove])
            max_len = max(max_len, right - left)
        return max_len

# Main.
if __name__ == "__main__":
    s = "aa"
    k = 1
    print(Solution().lengthOfLongestSubstringKDistinct(s, k))
