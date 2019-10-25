"""
Solution for Longest Substring with At Most K Distinct Characters, O(n).

Idea:
Using an ordered dict, so that pop min_val is O(1) instead of O(k).
Ordered dict is ordered by input order.
FIFO or LIFO if .pipitem(last=True or False)
"""

import collections

# Solution.
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        max_len = 0
        k_distinct = collections.OrderedDict()
        left = -1
        for right in range(len(s)):
            if s[right] in k_distinct:  # If s is already in dict, pop first to maintain order.
                k_distinct.pop(s[right])
            k_distinct[s[right]] = right
            if len(k_distinct) == k + 1:  # Too many.
                _, left = k_distinct.popitem(last=False)  # Pop first.
            max_len = max(max_len, right - left)
        return max_len

# Main.
if __name__ == "__main__":
    s = "abaccc"
    k = 2
    print(Solution().lengthOfLongestSubstringKDistinct(s, k))
