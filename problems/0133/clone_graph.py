"""
Solution for Clone Graph.

Idea:
DFS.
Maintain a copy_map from original to copy.
"""

class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

# Solution.
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        node_copy = Node(node.val, [])
        copy_map = {node: node_copy}
        stack = [node]
        while stack:
            current_node = stack.pop()
            for neighbor in current_node.neighbors:
                if neighbor not in copy_map:  # If this is a new node never visited before.
                    copy_map[neighbor] = Node(neighbor.val, [])  # Creates a copy.
                    stack.append(neighbor)  # To visit in the future.
                copy_map[current_node].neighbors.append(copy_map[neighbor])  # Links the node.
        return copy_map[node]

# Main.
if __name__ == "__main__":
    root = Node(1, [Node(2, [Node(4, []), Node(5, [])]), Node(3, [])])
    root_copy = Solution().cloneGraph(root)
    for n, ncopy in zip(root.neighbors, root_copy.neighbors):
        print(n.val, ncopy.val)
