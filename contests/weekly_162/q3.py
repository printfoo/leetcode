# DFS.

from __future__ import annotations

# Solution.
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            is_closed_island = 1
            queue = [(i, j)]
            while queue:
                i, j = queue.pop()
                grid[i][j] = 1  # Set to water.
                if i + 1 < r and grid[i + 1][j] == 0:
                    queue.append((i + 1, j))
                if i - 1 >= 0 and grid[i - 1][j] == 0:
                    queue.append((i - 1, j))
                if j + 1 < c and grid[i][j + 1] == 0:
                    queue.append((i, j + 1))
                if j - 1 >= 0 and grid[i][j - 1] == 0:
                    queue.append((i, j - 1))
                if i in {0, r - 1} or j in {0, c - 1}:
                    is_closed_island = 0  # This island is not closed.
            return is_closed_island

        if not grid:
            return 0
        r, c, closed_island_num = len(grid), len(grid[0]), 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    closed_island_num += dfs(i, j)
        return closed_island_num

# Main.
if __name__ == "__main__":
    grid = [[0,1,1,1,0],[1,0,1,0,1],[1,0,1,0,1],[1,0,0,0,1],[0,1,1,1,0]]
    print(Solution().closedIsland(grid))
