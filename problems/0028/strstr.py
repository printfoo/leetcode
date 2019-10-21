"""
Solution for Implement strStr(), O(n).

Idea:

"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hlen, nlen = len(haystack), len(needle)
        for i in range(hlen - nlen + 1):
            if haystack[i : i + nlen] == needle: return i
        return -1

# Main.
if __name__ == "__main__":
    haystack = "hello"
    needle = ""
    print(Solution().strStr(haystack, needle))
