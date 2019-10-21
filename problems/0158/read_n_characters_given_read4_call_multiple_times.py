"""
Solution for Read N Characters Given Read4 - Call multiple times.

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
    def __init__(self):
        self.residue = []

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Number of characters to read (int)
        :rtype: The number of actual characters read (int)
        """

        i = 0
        if n == 0:
            return 0

        while self.residue:
            buf[i] = self.residue.pop(0)
            i += 1
            if i == n:
                return i
            
        for _ in range( (n - len(self.residue)) // 4 + 1):
            buf4 = [" "] * 4
            read_n = read4(buf4)
            for j in range(read_n):
                if i < n:
                    buf[i] = buf4[j]
                    i += 1
                else:
                    self.residue.append(buf4[j])
        return i

# Main.
if __name__ == "__main__":
    file = list("abcdefghijklmno")
    solution = Solution()
    
    n = 2
    buf = [" "] * n
    read_n = solution.read(buf, n)
    print(read_n, buf, solution.residue)
    
    n = 1
    buf = [" "] * n
    read_n = solution.read(buf, n)
    print(read_n, buf, solution.residue)

    n = 0
    buf = [" "] * n
    read_n = solution.read(buf, n)
    print(read_n, buf, solution.residue)
    
    n = 2
    buf = [" "] * n
    read_n = solution.read(buf, n)
    print(read_n, buf, solution.residue)

    n = 5
    buf = [" "] * n
    read_n = solution.read(buf, n)
    print(read_n, buf, solution.residue)
    
    n = 10
    buf = [" "] * n
    read_n = solution.read(buf, n)
    print(read_n, buf, solution.residue)
