"""
Solution for Range Sum Query 2D - Immutable.

Idea:
Precomputation, given O(0,0) and any point P(p1,p2), compute OP.
Then ABCD = OD - OB - OC + OA
"""

from __future__ import annotations

# Solution.
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return None
        row_num = len(matrix) + 1  # One extra row.
        col_num = len(matrix[0]) + 1  # One extra column.
        self.areas = [[0 for j in range(col_num)] for i in range(row_num)]  # Initializes
        for i in range(1, row_num):
            for j in range(1, col_num):
                self.areas[i][j] = self.areas[i-1][j] + self.areas[i][j-1] - self.areas[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.areas[row2+1][col2+1] - self.areas[row2+1][col1] - self.areas[row1][col2+1] + self.areas[row1][col1]

# Main.
if __name__ == "__main__":
    matrix = [
      [3, 0, 1, 4, 2],
      [5, 6, 3, 2, 1],
      [1, 2, 0, 1, 5],
      [4, 1, 0, 1, 7],
      [1, 0, 3, 0, 5]
    ]
    obj = NumMatrix(matrix)
    for a in obj.areas:
        print(a)
    print(obj.sumRegion(2, 1, 4, 3))
    print(obj.sumRegion(1, 1, 2, 2))
    print(obj.sumRegion(1, 2, 2, 4))
