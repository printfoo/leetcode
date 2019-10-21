"""
Solution for Verifying an Alien Dictionary.

Idea:
"""

# solution
class Solution:
    def isAlienSorted(self, words, order) -> bool:
        order_map = {order[i]: i for i in range(len(order))}
        def isWordSorted(w1, w2):
            for c1, c2 in zip(w1, w2):
                if order_map[c1] < order_map[c2]: return True
                if order_map[c1] > order_map[c2]: return False
            return len(w1) <= len(w2)
        return all(isWordSorted(words[i], words[i + 1]) for i in range(len(words) - 1))

# Main.
if __name__ == "__main__":
    words = ["apple","app"]
    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(Solution().isAlienSorted(words, order))
