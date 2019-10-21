"""
Solution for Group Anagrams.

Idea:
Dictionary.
"""

from __future__ import annotations

# Solution
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in group_dict:
                group_dict[key] = [word]
            else:
                group_dict[key].append(word)
        return list(group_dict.values())

# Main.
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs))
