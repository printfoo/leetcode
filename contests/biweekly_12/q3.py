# This one doesn't work!

from __future__ import annotations
import collections

# Solution.
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        def search(start, end, visited):
            print(self.record)
            if start == end:
                return 0
            this_longest_dist = 0
            for edge in edges - visited:
                if start in edge:
                    next = edge[1 - edge.index(start)]
                    if (min(start, next), max(start, next)) in self.record:
                        return self.record[(min(start, next), max(start, next))]
                    visited.add(edge)
                    this_longest_dist = max(this_longest_dist, search(next, end, visited) + 1)
                    self.record[(min(start, next), max(start, next))] = this_longest_dist
            return this_longest_dist
    
        node_connections = []
        edges = {(min(edge), max(edge)) for edge in edges}
        for edge in edges:
            node_connections.extend(edge)
        node_counter = collections.Counter(node_connections)
        possible_ends = [node for node, count in node_counter.items() if count == 1]
        longest_dist = 0
        self.record = {}
        for node1 in possible_ends:
            for node2 in possible_ends:
                if node1 < node2:
                    longest_dist = max(longest_dist, search(node1, node2, {(node1, node2)}))
        return longest_dist

# Main.
if __name__ == "__main__":
    edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
    #edges = [[0,1],[1,2],[0,3],[2,4],[2,5],[0,6],[6,7],[3,8],[6,9],[2,10],[9,11],[4,12],[2,13],[1,14],[4,15],[9,16],[9,17],[9,18],[5,19],[15,20],[0,21],[8,22],[13,23],[17,24],[22,25],[20,26],[7,27],[22,28],[13,29],[16,30],[6,31],[9,32],[32,33],[18,34],[32,35],[15,36],[1,37],[35,38],[9,39],[21,40],[40,41],[10,42],[2,43],[43,44],[1,45],[10,46],[45,47],[42,48],[12,49],[8,50],[32,51],[7,52],[16,53],[51,54],[52,55],[46,56],[21,57],[46,58],[22,59],[24,60],[43,61],[11,62],[36,63],[37,64],[17,65],[32,66],[43,67],[67,68],[57,69],[9,70],[25,71],[53,72],[18,73],[30,74],[43,75],[49,76],[63,77],[27,78],[21,79],[3,80],[2,81],[41,82],[79,83],[35,84],[69,85],[34,86],[49,87],[2,88],[9,89],[84,90],[19,91],[10,92],[22,93],[11,94],[83,95],[42,96],[96,97],[25,98],[46,99],[47,100],[25,101],[50,102],[62,103],[101,104],[91,105],[22,106],[40,107],[7,108],[73,109],[95,110],[73,111],[82,112],[42,113],[110,114],[87,115],[15,116],[92,117],[117,118],[93,119],[102,120],[50,121],[48,122],[26,123],[27,124],[117,125],[123,126],[71,127]]
    print(Solution().treeDiameter(edges))
