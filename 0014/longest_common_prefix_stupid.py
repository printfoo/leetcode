"""
Stupid solution for Longest Common Prefix, O(mn).

Idea:
Compare from first to middle.
"""

# Solution.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        out_str = []
        try:
            strs[0]
        except IndexError:
            return ""
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                try:
                    if strs[0][i] != strs[j][i]:
                        return "".join(out_str)
                except IndexError:
                    return "".join(out_str)
            out_str.append(strs[0][i])
        return "".join(out_str)

# Main.
if __name__ == "__main__":
    strs = []
    solution = Solution()
    print(solution.longestCommonPrefix(strs))
