"""
Solution for Remove Invalid Parentheses, time O(2^n).

Idea:
DFS: from left to right as depth.
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
        
        def dfs_parentheses(current, left, right, removed, depth):

            if depth == len(s):  # ends recursion
                if left == right:  # valid
                    if removed < self.min_removed:
                        self.min_removed = removed  # update record
                        self.answer = {current}  # reset all records
                    elif removed == self.min_removed:
                        self.answer.add(current)  # add one to current record
            
            else:  # continues recursion
                if s[depth] not in {'(', ')'}:  # if not a parenthesis
                    # includes this char and adds depth by 1
                    dfs_parentheses(current+s[depth], left, right, removed, depth+1)
                else:  # if a parenthesis
                    # first tries to throw it away
                    dfs_parentheses(current, left, right, removed+1, depth + 1)
                    # then tries to include it
                    if s[depth] == '(':
                        dfs_parentheses(current+s[depth], left+1, right, removed, depth+1)
                    elif s[depth] == ')' and left > right:
                        # only if there is remaining left to match
                        dfs_parentheses(current+s[depth], left, right+1, removed, depth+1)

        dfs_parentheses(current='', left=0, right=0, removed=0, depth=0)
        return list(self.answer)

# Main.
if __name__ == '__main__':
    s = ''
    print(Solution().removeInvalidParentheses(s))
