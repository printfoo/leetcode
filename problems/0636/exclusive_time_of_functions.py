"""
Solution for Exclusive Time of Functions.

Idea:
Stack.
"""

from __future__ import annotations

# Solution.
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        exclusive_time = [0] * n
        stack = []
        prev_time = 0
        for log in logs:
            function_str, label, time_str = log.split(":")
            function, time = int(function_str), int(time_str)
            if not stack:  # If the begining.
                stack.append(function)
                continue
            if label == "start":
                function_to_count = stack[-1]  # The previous function.
                stack.append(function)  # This function, i.e., last-in function.
            else:
                time += 1  # start_time is reported at the begining of T but end time is at the end of T. We standardize time to the begining of T.
                function_to_count = stack.pop()  # function_to_count === function.
            exclusive_time[function_to_count] += time - prev_time  # Update exclusive time.
            prev_time = time  # Update prev_time record.
        return exclusive_time

# Main.
if __name__ == "__main__":
    n = 2
    logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
    print(Solution().exclusiveTime(n, logs))
