"""
Solution for Plus one.

Idea:
Plus one and carry
"""

# solution
class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix) < 2: return True
        else: return all(matrix[r][:-1] == matrix[r + 1][1:] for r in range(len(matrix) - 1))

# Main.
if __name__ == "__main__":
    matrix = [
              [84]
              ]
    print(Solution().isToeplitzMatrix(matrix))
