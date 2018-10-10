"""
Recursion solution for Evaluate Division, Each query O(n^2).

Idea:
x/y = x/a * a/b * b/c * ... * i/j * j/y
Note: for x/x if x in equations, return 1 else can't compute.
"""

# Solution.
class Solution:
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        def calc(source, target, info):
            for i in range(len(info)):
                e0, e1, v = info[i][0][0], info[i][0][1], info[i][1]
                if source == e0:
                    if source == target: return 1 # check if case x/x
                    if target == e1: return v # found
                    rest = calc(e1, target, info[:i] + info[i + 1:]) # check the rest
                    if rest: return v * rest
                if source == e1:
                    if source == target: return 1  # check if case x/x
                    if target == e0: return 1 / v # found, but need to reverse
                    rest = calc(e0, target, info[:i] + info[i + 1:]) # check the rest
                    if rest: return (1 / v) * rest
            return None

        res = [calc(q[0], q[1], [[e, v] for e, v in zip(equations, values)]) for q in queries]
        return [r if r else -1 for r in res]

# Main.
if __name__ == "__main__":
    equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
    values = [3.0,4.0,5.0,6.0]
    queries = [["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
    print(Solution().calcEquation(equations, values, queries))
