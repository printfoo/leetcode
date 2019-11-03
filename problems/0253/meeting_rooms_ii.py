"""
Solution for Meeting Rooms II, Time O(nlogn).

Idea:
Sort first, then priority queue.
"""

from __future__ import annotations
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        heap = [-float('inf')]
        intervals.sort()
        for interval in intervals:
            earliest_end = heap[0]
            if interval[0] >= earliest_end:
                heapq.heappushpop(heap, interval[1])
            else:
                heapq.heappush(heap, interval[1])
        return len(heap)

# Main.
if __name__ == "__main__":
    intervals = [[0,30],[5,10],[15,20]]
    print(Solution().minMeetingRooms(intervals))
