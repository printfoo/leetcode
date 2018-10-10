"""
Solution UTF-8 Validation, O(n).

Idea:
"""

# Solution.
class Solution:
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        data = ["{:08b}".format(d)[-8:] for d in data]
        while data:
            d = data.pop(0)
            if d[:1] == "0": continue
            elif d[:3] == "110":
                if len(data) < 1: return False
                for i in range(1):
                    if data.pop(0)[:2] != "10": return False
            elif d[:4] == "1110":
                if len(data) < 2: return False
                for i in range(2):
                    if data.pop(0)[:2] != "10": return False
            elif d[:5] == "11110":
                if len(data) < 3: return False
                for i in range(3):
                    if data.pop(0)[:2] != "10": return False
            else: return False
        return True

# Main.
if __name__ == "__main__":
    data = [237]
    print(Solution().validUtf8(data))
