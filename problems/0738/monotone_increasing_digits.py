"""
Solution for Monotone Increasing Digits.

Idea:
Find cliff and then xxx99...
"""

# Solution.
class Solution:
    def monotoneIncreasingDigits(self, N: int) -> int:
        n_str = str(N)
        for cliff in range(len(n_str)):
            if cliff == len(n_str) - 1:
                return N
            if n_str[cliff] > n_str[cliff + 1]:  # Char comparison, "5" > "3", etc.
                break  # Move right until find the first decreasing point.
        while cliff > 0:
            if n_str[cliff - 1] < n_str[cliff]:
                break  # Move left until different.
            cliff -= 1
        return int(n_str[:cliff] + str(int(n_str[cliff])-1) + "9"*(len(n_str)-cliff-1))

# Main.
if __name__ == "__main__":
    N = 123432
    print(Solution().monotoneIncreasingDigits(N))
