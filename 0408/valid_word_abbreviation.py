"""
Valid Word Abbreviation.

Idea:
Pay attention to:
- if loc is bigger than length of word.
- if ends with number
- if 0 in the string and is the first digit
"""

# Solution
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        loc, skip, word_len = 0, "0", len(word)
        for c in abbr:
            if c == "0" and skip == "0": return False # if skip start with 0 then false
            if not c.isnumeric():
                loc += int(skip)
                if loc >= word_len or word[loc] != c: return False
                skip = "0" # reset skip
                loc += 1 # loc move to next
            else: skip += c # counting skip
        return int(skip) == word_len - loc # in case ends with number

# Main.
if __name__ == "__main__":
    word = "internationalization"
    abbr = "i12iz5"
    print(Solution().validWordAbbreviation(word, abbr))
