"""
Solution for Interval List Intersections. Time O(m+n)

Idea:
"""

from __future__ import annotations


# solution
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        intersections = []
        ai = 0
        bi = 0
        while ai < len(A) and bi < len(B):
            left = max(A[ai][0], B[bi][0])
            right = min(A[ai][1], B[bi][1])
            if right >= left:
                intersections.append([left, right])
            if A[ai][1] == right:
                ai += 1
            if B[bi][1] == right:
                bi += 1
        return intersections

# Main.
if __name__ == "__main__":
    A = [[0,2],[5,10],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]
    print(Solution().intervalIntersection(A, B))
