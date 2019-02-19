"""
Solution for Sentence Similarity.

Idea:
"""

# solution
class Solution:
    def areSentencesSimilar(self, words1: "List[str]", words2: "List[str]", pairs: "List[List[str]]") -> "bool":
        if len(words1) != len(words2): return False
        for w1, w2 in zip(words1, words2):
            if w1 == w2: continue
            check = False
            for p in pairs:
                if p in [[w1, w2], [w2, w1]]: check = True
            if not check: return False
        return True

# Main.
if __name__ == "__main__":
    words1 = ["great", "acting", "skills"]
    words2 = ["fine", "drama", "talent"]
    pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]]
    print(Solution().areSentencesSimilar(words1, words2, pairs))