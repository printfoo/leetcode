"""
Solution for 3Sum Closest, O(n^2).

Idea:
Check from both end, head and tail. Sort first so ordered.
"""

# Solution.
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def recurseCombi(digits):
            if len(digits) == 0: return []
            elif len(digits) == 1: return [c for c in map[digits[0]]]
            else: return [c + p for p in recurseCombi(digits[1:]) for c in map[digits[0]]]

        map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        return recurseCombi(digits)

# Main.
if __name__ == "__main__":
    digits = ""
    print(Solution().letterCombinations(digits))
