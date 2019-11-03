# Each xy+xy or yx+yx needs 1 swap, residue needs 2 if any.


from __future__ import annotations

# Solution.
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy_counter = {"xy": 0, "yx": 0}
        if len(s1) != len(s2):
            return -1
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                xy_counter[c1 + c2] += 1
        if (xy_counter["xy"] + xy_counter["yx"]) % 2 != 0:
            return -1
        return xy_counter["xy"] // 2 + xy_counter["yx"] // 2 + xy_counter["xy"] % 2 + xy_counter["yx"] % 2

# Main.
if __name__ == "__main__":
    s1 = "xx"
    s2 = "xy"
    print(Solution().minimumSwap(s1, s2))
