"""
Solution for K Closest Points to Origin, Time O(nlogK).
Each heap push/pop is log(len(list)).
The list is of length K.
We did n pushes and K pops.

Idea:
Priority queue.
The optimization is to realize that heap[0] always stores the smallest element.
Instead of storing all n points, we need to store K.
Because we can keep replacing the one with the maximum distance.
Note 1: storing distance negatively.
Note 2: although heap[0] is the smallest, heap[-1] is NOT the largest.
"""

from __future__ import annotations
import heapq

# solution
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distance_heap = []
        for point in points:
            d = point[0] ** 2 + point[1] ** 2
            if len(distance_heap) < K:  # if not full, push only.
                heapq.heappush(distance_heap, (-d, point))
            else:  # if full, push and pop.
                heapq.heappushpop(distance_heap, (-d, point))
        return [_[1] for _ in distance_heap]

# Main.
if __name__ == "__main__":
    points = [[3,3],[5,-1],[-2,4]]
    K = 2
    print(Solution().kClosest(points, K))
