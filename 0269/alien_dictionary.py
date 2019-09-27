"""
Solution for Alien Dictionary.

Idea:
1. Build a DAG.
2. Topological sort.
Note: only words (ie leading chars) are sorted lexicographically,
not individual chars.
Note: using visited[] to make sure each node is traversed only once.
Note: using visiting[] to make sure no cycle, like a lock.
Corner case 1: words[i] is a prefix of words[i+1] -> shorter comes first
Corner case 2: unspecificed order -> random but needs to be iucluded
"""

from __future__ import annotations

# Solution.
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        # DFS for topological sort.
        def visit(from_node):
            if from_node in visited:  # if already visited stop visiting
                return True
            if from_node in visiting:  # if visiting, stop and add to cycles
                cycles.add(from_node)
                return False
            visiting.add(from_node)
            if from_node in graph:
                for to_node in graph[from_node]:
                    visit(to_node)  # DFS recursion
            alien_order.append(from_node)
            visited.add(from_node)
            visiting.remove(from_node)

        # Builds DAG.
        graph = {}
        all_chars = set("".join(words))  # remember all to add unordered chars later
        for i in range(len(words) - 1):
            if words[i].startswith(words[i + 1]) and len(words[i]) > len(words[i + 1]):
                return ""  # corner case of being prefix
            for char0, char1 in zip(words[i], words[i + 1]):
                if char0 == char1:
                    continue
                else:
                    if char0 not in graph:
                        graph[char0] = {char1}
                    else:
                        graph[char0].add(char1)
                    break
    
        # Topolofical sort.
        alien_order = []
        to_visit = set(graph.keys())
        visited = set()
        visiting = set()
        cycles = set()
        while to_visit:
            from_node = to_visit.pop()
            visit(from_node)
        if cycles:  # not a DAG
            return ""
        else:
            unordered = "".join(char for char in all_chars if char not in alien_order)
            return "".join(alien_order[::-1]) + unordered

# Main.
if __name__ == "__main__":
    words = ["wrt", "wrf", "er", "ett", "rftt"]
    words = ["ab","adc"]
    print(Solution().alienOrder(words))
