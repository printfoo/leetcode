"""
Solution for License Key Formatting O(n).

Idea:

"""

# Solution.
class Solution:
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        S = S.replace("-", "").upper()
        res, j = "", 0
        for i in range(len(S) - 1, -1, -1):
            res += S[i]
            j += 1
            if j == K and i != 0:
                res += "-"
                j = 0
        return res[::-1]

# Main.
if __name__ == "__main__":
    S = "2-5g-3-J"
    K = 2
    print(Solution().licenseKeyFormatting(S, K))
