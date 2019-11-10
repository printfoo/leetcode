# Aggregate by rows and columns.

from __future__ import annotations

# Solution.
class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        if not n or not m:
            return 0
        rows = [0] * n
        columns = [0] * m
        for row_i, column_i in indices:
            rows[row_i] = (rows[row_i] + 1) % 2
            columns[column_i] = (columns[column_i] + 1) % 2
        odd_count = 0
        for column in columns:
            if column == 0:
                odd_count += sum(rows)
            else:
                odd_count += len(rows) - sum(rows)
        return odd_count

# Main.
if __name__ == "__main__":
    n = 2
    m = 0
    indices = [[1,1],[0,0]]
    print(Solution().oddCells(n, m, indices))
