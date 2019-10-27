"""
Solution for Add and Search Word - Data structure design.

Idea:
Trie.
"""

# Definition for word node.
class WordNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        # Note that "is_word" is not equivalent to checking "not children".
        # For example, if "a" and "ab" are both words,
        # Then at "a", children = {"b": _} but "is_word = True".

# Solution.
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = WordNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        """
        stack = [[self.root, word]]
        while stack:
            node, word = stack.pop()
            if not word:  # If there is nothing to check.
                if node.is_word:  # If this is also the end of a word.
                    return True
            elif word[0] == ".":
                for child_char in node.children:
                    stack.append([node.children[child_char], word[1:]])
            elif word[0] in node.children:
                stack.append([node.children[word[0]], word[1:]])
        return False  # If checked all but no match.

# Main.
if __name__ == "__main__":

    obj = WordDictionary()
    obj.addWord("bad")
    obj.addWord("dad")
    obj.addWord("madd")
    #print(obj.search("pad"))
    #print(obj.search("bad"))
    print(obj.search("mad"))
    #obj.search("bad")
    #obj.search(".ad")
    #obj.search("b..")
