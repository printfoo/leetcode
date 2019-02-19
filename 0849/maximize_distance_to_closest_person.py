"""
Solution for Maximize Distance to Closest Person, Time O(n) Space O(1).

Idea:
Count 0s and divide 2.
"""

# solution
class Solution:
    def maxDistToClosest(self, seats: "List[int]") -> "int":
        middle, this, begin, end = 0, 0, 0, 0
        for s in seats:
            if s == 0: this += 1
            if s == 1:
                middle = max(middle, this)
                this = 0
        middle = max(middle, this)
        for s in seats:
            if s == 1: break
            begin += 1
        for s in seats[::-1]:
            if s == 1: break
            end += 1
        return max(begin, end, int((middle + 1) / 2))


# Main.
if __name__ == "__main__":
    seats = [1,0,0,0]
    print(Solution().maxDistToClosest(seats))
