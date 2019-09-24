"""
Solution for K Closest Points to Origin, Time O(nlogn).
Each heap push/pop is log(len(list)).
The list is of length n.
We did n pushes and K pops.

Idea:
Priority queue.
"""

from __future__ import annotations
import heapq

# solution
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance_heap = []
        for point in points:
            d = point[0] ** 2 + point[1] ** 2
            heapq.heappush(distance_heap, (d, point))
        kclosest = []
        for i in range(K):
            _, point = heapq.heappop(distance_heap)
            print(_, point)
            kclosest.append(point)
        return kclosest

# Main.
if __name__ == "__main__":
    points = [[3,3],[5,-1],[-2,4]]
    K = 2
    print(Solution().kClosest(points, K))
