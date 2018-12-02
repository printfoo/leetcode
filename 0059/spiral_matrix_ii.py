"""
Solution for Spiral Matrix II, Time O(n^2), Space O(n^2).

Idea:
Initialization first.
"""

# solution
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        m, i = [[None for _ in range(n)] for _ in range(n)], 0
        d = "r" # direction: right, down, left, up
        r, c = 0, 0 # current location
        br, bc, nr, nc = 0, 0, n - 1, n - 1 # borderline
        while i < n ** 2:
            i += 1
            if d == "r":
                m[r][c] = i; c += 1
                if c == nc:
                    d = "d" # change to down direction
                    br += 1; continue
            if d == "d":
                m[r][c] = i; r += 1
                if r == nr:
                    d = "l" # change to left direction
                    nc -= 1; continue
            if d == "l":
                m[r][c] = i; c -= 1
                if c == bc:
                    d = "u" # change to up direction
                    nr -= 1; continue
            if d == "u":
                m[r][c] = i; r -= 1
                if r == br:
                    d = "r" # change to right direction
                    bc += 1; continue
        return m

# Main.
if __name__ == "__main__":
    n = 5
    print(Solution().generateMatrix(n))
