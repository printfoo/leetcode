"""
Solution for Longest Arithmetic Sequence. Time O(n^2)

Idea:
Dynamic programming.
Maintain a 2D list dp[i][diff], recording at index i, with diff, the possible longest sequence.
Then the global max is the answer.
"""

from __future__ import annotations

# Solution.
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [{} for _ in A]
        longest = 0
        for i in range(len(A)):  # i from 0 to the end.
            for j in range(i):  # j from 0 to i.
                diff = A[i] - A[j]
                if diff not in dp[j]:  # If the diff between A[i] and A[j] is a new diff at j.
                    dp[i][diff] = 2  # Establishes a new record.
                else:  # If the diff between A[i] and A[j] follows another record at j.
                    dp[i][diff] = dp[j][diff] + 1  # Update that record by 1, i.e., add A[i].
                longest = max(dp[i][diff], longest)  # Updates global record.
        return longest

# Main.
if __name__ == "__main__":
    A = [9,4,7,2,10]
    print(Solution().longestArithSeqLength(A))
