"""
One Line Solution for Monotonic Array, Time O(n), Space O(1).

Idea:
Either increasing or decreasing
"""

# solution
class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        return all(A[i] <= A[i+1] for i in range(len(A) - 1)) or all(A[i] >= A[i+1] for i in range(len(A) - 1))

# Main.
if __name__ == "__main__":
    A = [1,3,2]
    print(Solution().isMonotonic(A))
