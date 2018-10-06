"""
Solution for Longest Absolute File Path, O(n).

Idea:
Scan line by line.
If . in line, reach end node, compare length and update max_length.
Otherwise, keep records of length in this branch.
"""

# Solution.
class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        lines = input.split("\n")
        max_len, depth_len = 0, {-1: 0}
        for line in lines:
            this_depth = sum([1 for c in line if c == "\t"]) # depth of this line
            this_len = len(line) - this_depth + 1 + depth_len[this_depth - 1] # length so far
            if "." in line and this_len > max_len: max_len = this_len
            else: depth_len[this_depth] = this_len
        return max_len - 1 if max_len >= 1 else 0 # first line has no \

# Main.
if __name__ == "__main__":
    input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
    print(Solution().lengthLongestPath(input))
