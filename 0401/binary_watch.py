"""
Recursion solution for Binary Watch.

Idea:
recurse on number of 0s and 1s.
"""

# Solution
class Solution:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def possibleLoc(n0, n1):
            possibility = []
            if n1 == 0: return [[0 for i in range(n0)]]
            if n0 == 0: return [[1 for i in range(n1)]]
            return [[1] + pos for pos in possibleLoc(n0, n1 - 1)] + [[0] + pos for pos in possibleLoc(n0 - 1, n1)]

        def getTime(pos):
            hour = sum([pos[i] << i for i in range(4)])
            min = sum([pos[i + 4] << i for i in range(6)])
            if hour < 12 and min < 60: return "{}:{:02d}".format(hour, min)
    
        possibility = possibleLoc(10 - num, num)
        times = []
        for pos in possibility:
            time = getTime(pos)
            if time: times.append(time)
        return times


# Main.
if __name__ == "__main__":
    num = 2
    expected = ["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"]
    expected.sort()
    solution = Solution().readBinaryWatch(num)
    solution.sort()
    print(solution)
    print(expected)
