"""
Solution for Friends of Appropriate Ages, Time O(n^2).

Idea:
Counter age and interate.
"""

from __future__ import annotations
import collections

# solution
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        friends = 0
        people = collections.Counter(ages)
        for A in people:
            for B in people:
                if B > 0.5 * A + 7 and B <= A:
                    if B != A:
                        friends += people[B] * people[A]
                    else:
                        friends += people[B] * (people[A] - 1)
        return friends
                

# Main.
if __name__ == "__main__":
    ages = [20,30,100,110,120]
    print(Solution().numFriendRequests(ages))
