"""
Stupid solution for Reverse String, O(n).

Idea:
Diectly reverse.
"""

# Solution.
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        out_s = []
        len_s = len(s)
        for i in range(len_s):
            out_s.append(s[len_s - 1 - i])
        return "".join(out_s)

# Main.
if __name__ == "__main__":
    s = "hello"
    print Solution().reverseString(s)
