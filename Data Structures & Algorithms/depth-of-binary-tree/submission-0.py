# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Problem Explanation
The depth (or maximum depth) of a binary tree is the length of the longest path from the root node to any leaf node. We measure depth by counting the number of nodes along this path.

Key points:

An empty tree (no nodes) has depth 0
A tree with just the root node has depth 1
We need to find the longest path from root to any leaf
Example 1 visualization:

    1
   / \
  2   3
     /
    4
The longest path is 1 → 3 → 4, which has 3 nodes, so depth = 3.

Solution Approaches
There are three common approaches:

Recursive DFS (most intuitive)
Iterative DFS (using a stack)
BFS (using a queue, level by level)
Here's the most common recursive solution with detailed comments:
'''

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: if the node is None (empty tree or leaf's child)
        if not root:
            return 0
        
        # Recursively find the depth of left subtree
        left_depth = self.maxDepth(root.left)
        
        # Recursively find the depth of right subtree
        right_depth = self.maxDepth(root.right)
        
        # The depth at current node is 1 (for current node) 
        # plus the maximum of left and right subtree depths
        return 1 + max(left_depth, right_depth)