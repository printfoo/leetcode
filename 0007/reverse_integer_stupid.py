"""
Stupid solution for Reverse Interger, O(n).

Idea:
Cast to string and reverse.
"""

# Solution.
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        out_str = []
        str_x = str(x)
        if str_x[0] == "-":
            sign = "-"
            str_x = str_x[1:]
        else:
            sign = ""
        len_x = len(str_x)
        for i in range(len_x):
            out_str.append(str_x[len_x - 1 - i])
        x = int(sign + "".join(out_str))
        if x > 2 ** 31 - 1 or x < -2 ** 31:
            return 0
        return x

# Main.
if __name__ == "__main__":
    x = -15342364
    solution = Solution()
    print solution.reverse(x)
