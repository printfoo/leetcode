"""
Stupid solution for Count and Say.

Idea:
Recurse.
"""

# Solution.
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n > 1:
            previous = self.countAndSay(n - 1)
            say = previous[0]
            count = 0
            s = ""
            for e in previous:
                if e == say:
                    count += 1
                else:
                    s += str(count) + say # refresh
                    say = e
                    count = 1
            s += str(count) + say # last one
            return s
        else:
            return "1"

# Main.
if __name__ == "__main__":
    n = 6
    solution = Solution()
    print(solution.countAndSay(n))
