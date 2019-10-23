"""
Solution for Minimum Window Substring, Time O(n).

Idea:
Sliding Window.
"""

import collections

# solution
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        needs = collections.Counter(t)
        missing = len(t)
        current_left = 0
        final_left = 0
        final_right = float("inf")
        for current_right, char_right in enumerate(s): # Matches string.
            if char_right in needs:  # If the char is needed.
                needs[char_right] -= 1  # Needs one less, can be negative.
                if needs[char_right] >= 0:  # If this one is not over-matched.
                    missing -= 1  # Then one less missing char.
            if not missing:  # If no more missing chars.
                while current_left < current_right: # Contracts window.
                    char_left = s[current_left]
                    if char_left in needs:  # If the char is needed.
                        needs[char_left] += 1  # Cancel overmatch by one.
                        if needs[char_left] > 0:  # If needed more than 0 (canceled too many).
                            missing += 1  # Missing one more (this char).
                            break  # Refreshes and starts another round.
                    current_left += 1
                if final_right - final_left > current_right - current_left:  # Refreshes min.
                    final_right = current_right
                    final_left = current_left
                current_left += 1  # Move current left pointer by 1 to continue.
        return s[final_left: final_right + 1] if final_right < len(s) else ""

# Main.
if __name__ == "__main__":
    S = "ABAACBAB"
    T = "ABC"
    S = "a"
    T = ""
    print(Solution().minWindow(S, T))
