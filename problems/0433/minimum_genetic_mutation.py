"""
Solution for Minimum Genetic Mutation.

Idea:

"""

# Solution
class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        
        def mutate(start, end, bank, i):
            if start == end: return nums.append(i)
            if not bank and start != end: return 0
            for b in bank:
                diff = sum(1 for i, j in zip(b, start) if i != j)
                if diff == 1: mutate(b, end, bank - {b}, i + 1)

        nums, bank = [], set(bank)
        mutate(start, end, bank, 0)
        return min(nums) if nums else -1

# Main.
if __name__ == "__main__":
    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGATT","AACCGATA","AAACGATA","AAACGGTA"]
    print(Solution().minMutation(start, end, bank))
