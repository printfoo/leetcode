# First assign 0 and 2, then assign remaining 1s.

from __future__ import annotations

# Solution.
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        m = [[0] * len(colsum), [0] * len(colsum)]
        for i, sum_i in enumerate(colsum):
            if sum_i == 2:
                m[0][i] = 1
                upper -= 1
                m[1][i] = 1
                lower -= 1
        if upper < 0 or lower < 0:
            return []
        for i, sum_i in enumerate(colsum):
            if sum_i == 1:
                if upper > 0:
                    m[0][i] = 1
                    upper -= 1
                    m[1][i] = 0
                elif lower > 0:
                    m[1][i] = 1
                    lower -= 1
                    m[0][i] = 0
                else:
                    return []
        return m if upper == lower == 0 else []
        

# Main.
if __name__ == "__main__":
    upper = 5
    lower = 5
    colsum = [2,1,2,0,1,0,1,2,0,1]
    m = Solution().reconstructMatrix(upper, lower, colsum)
    limit = [upper, lower]
    for i, row in enumerate(m):
        print(row, limit[i])
    print(colsum)
