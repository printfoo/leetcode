"""
Solution for Backspace String Compare, Time O(n), Space O(1).

Idea:
Check one by one.

Note:
Check index of list often because python can use negative index
"""

# solution
class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        i, j = len(S) - 1, len(T) - 1
        back_S, back_T = 0, 0
        
        while i >= 0 or j >= 0:
            # back S
            if i >= 0 and S[i] == "#":
                back_S += 1
                i -= 1
                continue
            elif back_S > 0:
                back_S -= 1
                i -= 1
                continue

            # back T
            if j >= 0 and T[j] == "#":
                back_T += 1
                j -= 1
                continue
            elif back_T > 0:
                back_T -= 1
                j -= 1
                continue
            
            # compare
            if i >= 0 and j >= 0 and S[i] != T[j]: return False # not equal
            if (i < 0 and j >= 0) or (j < 0 and i >= 0): return False # one of the list is empty
            i -= 1
            j -= 1

        return True

# Main.
if __name__ == "__main__":
    S = "baaa#####a"
    T = "abaaa#####a"
    print(Solution().backspaceCompare(S, T))
