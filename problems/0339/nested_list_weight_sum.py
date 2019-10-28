"""
Solution for Nested List Weight Sum. Time O(n).

Idea:
DFS.
"""

from __future__ import annotations

# Solution.
class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        stack = [[_, 1] for _ in nestedList]
        depth_sum = 0
        while stack:
            nest, depth = stack.pop()
            if nest.isInteger():
                depth_sum += nest.getInteger() * depth
            else:
                stack.extend([_, depth + 1] for _ in nest.getList())
        return depth_sum

# Main.
if __name__ == "__main__":
    nestedList = [[1,1],2,[1,1]]
    print(Solution().depthSum(nestedList))
