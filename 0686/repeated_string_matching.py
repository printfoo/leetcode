"""
Solution for Repeated String Matching O(n).

Idea:
B has to be shorter than or equal to tA.
If B not in tA or (t+1)A, B not in (any)A.

Proof:
If B not in tA, B could match [A-, tA+] because the interval could be smaller than tA.
If B not in (t+1)A, B could not match [A-, (t+1)A+] because such interval in bigger than tA >= B.
Therefore, if B not in (t+1)A, B cannot be matching by (any)A.
"""

# Solution.
class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        t = -(-len(B) // len(A)) # ceil
        if B in A * t: return t
        elif B in A * (t + 1): return t + 1
        else: return -1

# Main.
if __name__ == "__main__":
    A = "abcd"
    B = "cdabcdab"
    print(Solution().repeatedStringMatch(A, B))
