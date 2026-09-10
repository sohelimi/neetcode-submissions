# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Binary Tree Maximum Path Sum - Full Explanation
Problem Understanding
You need to find the maximum sum of any path in a binary tree, where:

A path is a sequence of connected nodes (parent-child relationships)
Each node appears at most once
The path doesn't have to include the root
We want to maximize the sum of node values along any valid path
Key insight: A path can go through a node in two ways:

Straight down one side (left or right child)
Through the node connecting left and right subtrees (like a bridge)
For example, in [1,2,3], the path 2→1→3 passes through node 1, combining both left and right subtrees.

Approach: Post-Order DFS
We use DFS to traverse the tree bottom-up, tracking:

Maximum path sum through any node (could bend at that node)
Maximum path sum that can extend upward from each node (straight line)
Key Distinction:
Return value: Maximum sum from current node down to one child (can be extended upward)
Global result: Maximum sum including paths that bend/connect at a node
Full Solution with Comments
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize result with root value (minimum valid path)
        res = [root.val]
        
        def dfs(node):
            # Base case: empty node contributes 0
            if not node:
                return 0
            
            # Recursively get max path sum from left and right subtrees
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            
            # Ignore negative contributions from subtrees
            # (we can always skip a negative path)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            
            # OPTION 1: Path goes THROUGH this node (bends here)
            # Include node value + both subtree paths
            pathThroughNode = node.val + leftMax + rightMax
            res[0] = max(res[0], pathThroughNode)
            
            # OPTION 2: Path goes STRAIGHT DOWN
            # Return the best single path that can extend to parent
            # Include this node + better of left/right subtree
            return node.val + max(leftMax, rightMax)
        
        dfs(root)
        return res[0]

'''
Walkthrough Example
For tree [1,2,3]:

      1
     / \
    2   3
Visit node 2 (leaf):

leftMax = 0, rightMax = 0
pathThroughNode = 2 + 0 + 0 = 2, update res[0] = 2
Return 2 (can extend upward)
Visit node 3 (leaf):

Same logic: pathThroughNode = 3, update res[0] = 3
Return 3
Visit node 1 (root):

leftMax = 2, rightMax = 3
Both positive, so keep them
pathThroughNode = 1 + 2 + 3 = 6, update res[0] = 6 ✓
Return 1 + max(2, 3) = 4
Answer: 6 ✓

Complex Example: [-15, 10, 20, null, null, 15, 5, -5]
        -15
        /  \
       10   20
          /  \
         15   5
         /
       -5
When we reach node 20:

leftMax = 15 (path: 15 → 20 gives 35)
rightMax = 5
pathThroughNode = 20 + 15 + 5 = 40 ← This is the answer!
Return 20 + max(15, 5) = 35
Complexity Analysis
Time: O(n) - Visit each node once
Space: O(h) - Recursion stack, where h is height (worst case O(n) for skewed tree)
The solution elegantly handles negative numbers by allowing us to skip paths with negative sums!
'''