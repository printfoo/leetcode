"""
Solution for Longest Substring with At Most Two Distinct Characters, Time O(n), Space O(1).

Idea:
Maintain a window.
(This solution is easy to understand.)
"""

# Solution.
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: "str") -> "int":
        max_len = 0
        two_distinct = {}
        left = -1  # Left pointer starts from -1 because "aaa" should be 2-(-1).
        for right in range(len(s)):  # Right pointer keep updating "abc" should be 2-0.
            two_distinct[s[right]] = right
            if len(two_distinct) == 3:  # If too many.
                index_to_remove = min(two_distinct.values())
                left = two_distinct.pop(s[index_to_remove])  # Remove the leftist one.
            max_len = max(max_len, right - left)
        return max_len
        
# Main.
if __name__ == "__main__":
    s = ""
    print(Solution().lengthOfLongestSubstringTwoDistinct(s))
