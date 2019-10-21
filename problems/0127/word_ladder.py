"""
Solution for Word Ladder.

Idea:
BFS, all possible word variates O(26 L^2 N), not wordList O(L N^2).
Should not do DFS, because first answer find in BFS always works.
"""

# Solution.
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet, wordLen = set(wordList), len(beginWord)
        queue = [(beginWord, 1)]
        while queue:
            word, ladderLen = queue.pop(0)
            if word == endWord: return ladderLen
            for c in "abcdefghijklmnopqrstuvwxyz":
                for i in range(wordLen):
                    tempWord = word[:i] + c + word[i+1:] # temporarily save
                    if tempWord in wordSet:
                        wordSet.remove(tempWord) # every possibility only visit once
                        queue.append([tempWord, ladderLen + 1])
        return 0


# Main.
if __name__ == "__main__":
    beginWord = "qa"
    endWord = "sq"
    wordList = ["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]
    print(Solution().ladderLength(beginWord, endWord, wordList))
