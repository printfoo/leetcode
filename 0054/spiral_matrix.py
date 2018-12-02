"""
Solution for Spiral Matrix, Time O(mn), Space O(mn).

Idea:
Simple traverse.
"""

# solution
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        spiral = []
        while matrix:
            spiral.extend(matrix.pop(0))
            for row in matrix:
                if row: spiral.append(row.pop(-1))
            if matrix: spiral.extend(matrix.pop(-1)[::-1])
            for row in matrix[::-1]:
                if row: spiral.append(row.pop(0))
        return spiral

# Main.
if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(Solution().spiralOrder(matrix))
