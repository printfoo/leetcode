"""
Solution for longest uncommon subsequence, O(n).

Idea:
"""

class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        return -1 if a == b else max(len(a), len(b))

# Main.
if __name__ == "__main__":
    a = "horbxeemlgqpqbujbdagizcfairalg"
    b = "iwvtgyojrfhyzgyzeikqagpfjoaeen"
    print(Solution().findLUSlength(a, b))
