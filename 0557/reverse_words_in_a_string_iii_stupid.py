"""
Stupid solution for Reverse Words in a String III, O(n).

Idea:
Use a word to remember word, use another list to remember space.
"""

# Solution.
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        def reverseAWord(word):
            return "".join([word[len(word) - i - 1] for i in range(len(word))])
        s = s + " "
        word = []
        out = []
        for letter in s:
            if letter != " ":
                word.append(letter)
            else:
                out.append(reverseAWord(word))
                word = []
        return " ".join(out)

# Main.
if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    solution = Solution()
    print(solution.reverseWords(s))
