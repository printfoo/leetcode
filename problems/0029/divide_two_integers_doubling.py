"""
Solution for Divide Two Integers, O(log(n)).

Idea:
Keep doubling divisor until found the biggest one, then next biggest one, etc.
"""

# Solution.
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor, quotient = abs(dividend), abs(divisor), 0
        while dividend >= divisor:
            divisor_temp = divisor
            quotient_temp = 1
            while dividend >= divisor_temp + divisor_temp: # find the largest multiples of divisions
                divisor_temp += divisor_temp
                quotient_temp += quotient_temp
            dividend -= divisor_temp # minues the biggest one and find again
            quotient += quotient_temp
        if (not positive and quotient > 2147483648) or (positive and quotient > 2147483647): return 2147483647
        else: return quotient if positive else -quotient

# Main.
if __name__ == "__main__":
    dividend = -2147483648
    divisor = 1
    solution = Solution()
    print(solution.divide(dividend, divisor))
