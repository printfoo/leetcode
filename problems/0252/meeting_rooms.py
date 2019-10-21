"""
Solution for Meeting Rooms, Time O(n).

Idea:
Sort first, then a meeting need to ends before the next starts.
"""

# Solution.
class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort()
        return all(intervals[i][1] <= intervals[i + 1][0] for i in range(len(intervals) - 1))

# Main.
if __name__ == "__main__":
    intervals = [[13,15],[1,13]]
    print(Solution().canAttendMeetings(intervals))
