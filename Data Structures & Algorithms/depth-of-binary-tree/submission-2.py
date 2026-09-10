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

'''
How the Recursive Solution Works
Let's trace through the example [1,2,3,null,null,4]:

    1
   / \
  2   3
     /
    4
Start at node 1:

Left subtree depth = maxDepth(node 2)
Right subtree depth = maxDepth(node 3)
Return 1 + max(1, 2) = 3
At node 2:

Left child is None → returns 0
Right child is None → returns 0
Return 1 + max(0, 0) = 1
At node 3:

Left subtree depth = maxDepth(node 4)
Right child is None → returns 0
Return 1 + max(1, 0) = 2
At node 4:

Left child is None → returns 0
Right child is None → returns 0
Return 1 + max(0, 0) = 1
Complexity Analysis
Time Complexity: O(n) where n is the number of nodes (we visit each node once)
Space Complexity: O(h) where h is the height of the tree (for the recursion call stack)
Alternative Solutions
If you prefer iterative approaches:

BFS (Level Order Traversal):
'''

'''
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        q = deque([root])
        depth = 0
        
        while q:
            # Process all nodes at current level
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            depth += 1  # Increment after processing each level
        
        return depth

#Iterative DFS:

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]  # [node, current_depth]
        max_depth = 0
        
        while stack:
            node, depth = stack.pop()
            
            if node:
                max_depth = max(max_depth, depth)
                # Add children with increased depth
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return max_depth
#The recursive DFS is usually preferred for its simplicity and readability for this problem.
'''
