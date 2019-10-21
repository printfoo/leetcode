"""
Solution for Find All Anagrams in a String, Time O(n), Space O(1).

Idea:
Sliding window.
"""

# Solution
class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        anagrams, len_s, len_p, letters = [], len(s), len(p), "abcdefghijklmnopqrstuvwxyz"
        p_dict, s_dict = {c: 0 for c in letters}, {c: 0 for c in letters}
        for c in p: p_dict[c] += 1
        for c in s[:len_p]: s_dict[c] += 1
        if s_dict == p_dict: anagrams.append(0) # first 0
        for i in range(1, len_s - len_p + 1): # sliding window from 1
            s_dict[s[i - 1]] -= 1
            s_dict[s[i + len_p - 1]] += 1
            if s_dict == p_dict: anagrams.append(i)
        return anagrams

# Main.
if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s, p))
