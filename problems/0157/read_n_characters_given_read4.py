"""
Solution for Read N Characters Given Read4.

Idea:
"""

def read4(buf):
    if not file:
        return 0
    for i in range(4):
        buf[i] = file.pop(0)
        if not file:
            break
    return i + 1

# Solution.
class Solution:
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """
        i = 0
        for _ in range(n//4+1):
            buf4 = [" "] * 4
            read_n = read4(buf4)
            for j in range(read_n):
                if i < n:
                    buf[i] = buf4[j]
                    i += 1
        return i

# Main.
if __name__ == "__main__":
    file = list("abcdefg")
    solution = Solution()
    n = 10
    buf = [" "] * n
    read_n = solution.read(buf, n)
    print(read_n, buf)
