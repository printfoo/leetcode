"""
Solution for Add Binary.

Idea:
"""

# solution
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = [int(_) for _ in list(a)], [int(_) for _ in list(b)]
        res, carry = [], 0
        while a or b:
            a0 = a.pop() if a else 0
            b0 = b.pop() if b else 0
            res0 = a0 + b0 + carry
            if res0 < 2:
                res.append(res0)
                carry = 0
            else:
                res.append(res0 - 2)
                carry = 1
        if carry == 1: res.append(carry)
        res.reverse()
        return "".join([str(r) for r in res])


# Main.
if __name__ == "__main__":
    a = "11"
    b = "1"
    print(Solution().addBinary(a, b))
