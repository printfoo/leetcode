"""
Solution for Merge Intervals, Time O(nlogn).

Idea:
Sort.
"""

from __future__ import annotations

# Solution.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merged = []
        start, end = -float("inf"), -float("inf")
        for interval in intervals:
            if interval[0] > end:  # Disconnected.
                merged.append([start, end])  # Finishes current interval.
                start, end = interval  # Starts another interval.
            else:  # Connected.
                end = max(interval[1], end)  # Update end of current interval.
        merged.append([start, end])  # Last one.
        return merged[1:]
    

# Main.
if __name__ == "__main__":
    intervals = [[1,4],[2,3]]
    print(Solution().merge(intervals))
