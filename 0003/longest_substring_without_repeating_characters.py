"""
Solution for Longest Substring Without Repeating Characters, O(n).

Idea:
Use a dict to save index, and keep tracking current length and max length.
For current length, use "start" to store where to count, and if a duplicated letter is found, "start" move to the next location where the letter is found.
Since updating set or list is too complated, we use a dict and check only if the location of the letter is found after "start" (real duplicated).
"""

# Solution.
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, maxLen, charDict = 0, 0, {}
        for i, c in enumerate(s):
            if c in charDict and charDict[c] >= start: start = charDict[c] + 1
            maxLen = max(maxLen, i - start + 1)
            charDict[c] = i
        return maxLen

# Main.
if __name__ == "__main__":
    s = "pwwkew"
    print(Solution().lengthOfLongestSubstring(s))
