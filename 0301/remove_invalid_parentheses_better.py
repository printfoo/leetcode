"""
Solution for Remove Invalid Parentheses, time O(2^n).
The worse time is still O(2^n) but added constrain so it is faster on average.

Idea:
DFS: from left to right as depth.
First count how many left and right needed to be removed.
"""

# Solution.
class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.min_removed = float('inf')
        self.answer = set()
        left_remain = 0  # eventually should remove this number of left
        right_remain = 0  # eventually should remove this number of right
        for c in s:
            if c == '(':
                left_remain += 1
            elif c == ')':
                if left_remain:
                    left_remain -= 1
                else:
                    right_remain += 1
        
        def dfs_parentheses(current, left, right, left_remain, right_remain, depth):

            if depth == len(s):  # ends recursion
                if left == right and left_remain == right_remain == 0:
                    # valid and removed the exact number of left and right
                    self.answer.add(current)  # add one to current record
            
            else:  # continues recursion
                if s[depth] not in {'(', ')'}:  # if not a parenthesis
                    # includes this char and adds depth by 1
                    dfs_parentheses(current+s[depth], left, right, left_remain, right_remain, depth+1)
                else:  # if a parenthesis
                    if s[depth] == '(':
                        if left_remain > 0:  # tries to remove it only when we can
                            dfs_parentheses(current, left, right, left_remain-1, right_remain, depth+1)
                        dfs_parentheses(current+s[depth], left+1, right, left_remain, right_remain, depth+1)
                    else:
                        if right_remain > 0:  # tries to remove it only when we can
                            dfs_parentheses(current, left, right, left_remain, right_remain-1, depth+1)
                        if left > right:  # only if there is remaining left to match
                            dfs_parentheses(current+s[depth], left, right+1, left_remain, right_remain, depth+1)

        dfs_parentheses(current='', left=0, right=0,
                        left_remain=left_remain, right_remain=right_remain, depth=0)
        return list(self.answer)

# Main.
if __name__ == '__main__':
    s = ')(())('
    print(Solution().removeInvalidParentheses(s))
