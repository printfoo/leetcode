"""
Solution for Isomorphic Strings.

Idea:
1 to N and N to 1 all return False, therefore keep 2 dicts, mapping and mapped.
"""

# Solution.
class Solution:
    def isIsomorphic(self, s: "str", t: "str") -> "bool":
        mapping, mapped = {}, {}
        if len(s) != len(t): return False
        for cs, ct in zip(s, t):
            if (cs in mapping and mapping[cs] != ct) or (ct in mapped and mapped[ct] != cs): return False
            mapping[cs], mapped[ct] = ct, cs
        return True


# Main.
if __name__ == "__main__":
    s = "ab"
    t = "aa"
    print(Solution().isIsomorphic(s, t))
