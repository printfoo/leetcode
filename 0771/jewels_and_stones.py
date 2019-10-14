"""
Solution for Jewels and Stones.

Idea:
"""

# solution
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return len([s for s in S if s in J])

# Main.
if __name__ == "__main__":
    J = "aA"
    S = "aAAbbbb"
    print(Solution().numJewelsInStones(J, S))
