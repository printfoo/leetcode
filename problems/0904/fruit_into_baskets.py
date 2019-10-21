"""
Solution for Fruit Into Baskets, Time O(n), Space O(1).

Idea:
Keep remembering where to start, where to end, where type changes, and max fruit selected and ordered baskets.
"""

# solution
class Solution:
    def totalFruit(self, tree: "List[int]") -> "int":
        start, end, change, maxfruit, baskets = 0, 0, 0, 0, [None, None]
        for t in tree:
            if t not in baskets: maxfruit, start, change = max(maxfruit, end - start), change, end
            if t != baskets[1]: change, baskets = end, [baskets[1], t]
            end += 1
        return max(maxfruit, end - start)

# Main.
if __name__ == "__main__":
    A = [1,2,3,2,2]
    print(Solution().totalFruit(A))
