"""
Solution for Merge BSTs, Time O(max(n)), Space O(max(h_n)).

Idea:
Inorder interation.
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Solution.
class Solution(object):
    def merge(self, roots):
    
        # Move pointer to leftist and add nodes on the way to stacks.
        tree_nums = len(roots)
        stacks = [[] for _ in range(tree_nums)]
        for i in range(tree_nums):  # For each tree.
            while roots[i]:  # While node is not empty.
                stacks[i].append(roots[i])  # Add this node to stack.
                roots[i] = roots[i].left  # Move pointers to the left.
        
        # Interatively add smallest elements to ans until all is empty.
        ans = []
        while any(stacks):  # When at least one stack is not empty.
            nodes_map = {}  # A nodes_map of {val: i} so we can find which tree has min.
            for i in range(tree_nums):
                if stacks[i]:
                    nodes_map[stacks[i][-1].val] = i
            selected_tree = nodes_map[min(nodes_map)]  # Select the tree with min.
            selected_node = stacks[selected_tree].pop()  # Get the node with min.
            ans.append(selected_node.val)  # Add min the ans.
            to_add_node = selected_node.right  # Next to add node is current nodes right child.
            while to_add_node:  # If such right child exist.
                stacks[selected_tree].append(to_add_node)  # Add this child.
                to_add_node = to_add_node.left  # And keep moving pointers to the left.

        return ans


# Main.
if __name__ == "__main__":

    root0 = TreeNode(8)
    root0.left = TreeNode(2)
    root0.right = TreeNode(10)
    root0.left.left = TreeNode(1)

    root1 = TreeNode(5)
    root1.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.left.left = TreeNode(0)
    
    root2 = TreeNode(15)
    root2.left = TreeNode(12)
    
    root3 = TreeNode(50)
    root3.right = TreeNode(100)
    
    print(Solution().merge([root0, root1, root2, root3]))
