"""
Solution for Task Scheduler, Time O(n), n = # of tasks.

Idea:
Priority Queue.
Because there are only up to 26 tasks so a lot of operations are O(1).
But this is slow nontheless, comparing to the mathmatical solution.
Note: don't store the order.
"""

import heapq
import collections

# Solution.
class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # Initializes the heap.
        to_schedule = []
        for task, freq in collections.Counter(tasks).items():
            heapq.heappush(to_schedule, [-freq, task])  # min heap
        
        # Traverses the heap.
        intervals = 0
        while to_schedule:
            temp = []
            for i in range(n + 1):
                if not to_schedule and not temp:  # if nothing left
                    break  # break the loop, stop counting
                intervals += 1
                if not to_schedule:  # if nothing can be scheduled this round
                    continue  # counting as idle
                neg_freq, task = heapq.heappop(to_schedule)
                if neg_freq != -1:
                    temp.append([neg_freq + 1, task])
            for neg_freq, task in temp:  # push all temporary ones to heap
                heapq.heappush(to_schedule, [neg_freq, task])
        return intervals

# Main.
if __name__ == "__main__":
    tasks = ["A","A","A","B","B","C"]
    n = 2
    print(Solution().leastInterval(tasks, n))
