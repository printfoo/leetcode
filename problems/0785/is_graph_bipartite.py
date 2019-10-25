"""
Solution for Is Graph Bipartite.

Idea:
Coloring + DFS.
"""

from __future__ import annotations

# Solution.
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colored_nodes = {}
        for node, neighbors in enumerate(graph):
            if node in colored_nodes:  # If already colored, pass.
                continue
            colored_nodes[node] = 1  # Colors this node with 1.
            stack = [[node, neighbors]]
            while stack:
                this_node, this_neighbors = stack.pop()
                for neighbor in this_neighbors:
                    if neighbor not in colored_nodes:  # If neighbor is not colored.
                        colored_nodes[neighbor] = -1 * colored_nodes[this_node] # Colors neighbor with opposite -1.
                        stack.append([neighbor, graph[neighbor]])  # Add neighbor to visit next.
                    elif colored_nodes[neighbor] == colored_nodes[this_node]:  # If neighbor is colored, but the same.
                        return False  # Not bipartite.
        return True  # No conflicts.

# Main.
if __name__ == "__main__":
    graph = [[1,2,3], [0,2], [0,1,3], [0,2]]
    print(Solution().isBipartite(graph))
