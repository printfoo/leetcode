"""
Solution for Task Scheduler, Time O(n), n = # of tasks.

Idea:
The final task can only be 2 cases.
1. If there is ANY idle, then the time is depended on most frequent taskS.
2. If there is NO idle, then the time is intuitively len(tasks).
So the time must be max(case1, case2).
https://leetcode.com/problems/task-scheduler/discuss/104507/Python-Straightforward-with-Explanation
"""

import collections

# Solution.
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = list(collections.Counter(tasks).values())
        most_frequent = max(counter)
        most_frequent_tasks = counter.count(most_frequent)
        intervals_if_any_idle = (most_frequent - 1) * (n + 1) + most_frequent_tasks
        intervals_if_no_idle = len(tasks)
        return max(intervals_if_any_idle, intervals_if_no_idle)

# Main.
if __name__ == "__main__":
    tasks = ["A","A","A","B","B","C"]
    n = 2
    print(Solution().leastInterval(tasks, n))
