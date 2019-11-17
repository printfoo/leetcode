# Iteration.

from __future__ import annotations

# Solution.
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def shift(grid):
            shifted_grid = [row[-1:] + row[:-1] for row in grid]
            last = shifted_grid[-1][0]
            for row in shifted_grid:
                row[0], last = last, row[0]
            return shifted_grid
    
        for _ in range(k):
            grid = shift(grid)
        return grid
        

# Main.
if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 9
    print(Solution().shiftGrid(grid, k))
