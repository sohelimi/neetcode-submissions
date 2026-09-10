# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Problem Explanation
We need to determine if two binary trees are identical - meaning they have:

Same structure: Nodes appear in the same positions
Same values: Corresponding nodes have equal values
Key Insight
We can solve this using depth-first search (DFS) to traverse both trees simultaneously and compare nodes at each position.

Solution Approach
We'll use recursion to check:

If both nodes are None → return True (base case)
If one node is None and the other isn't → return False (structure mismatch)
If both nodes exist but have different values → return False (value mismatch)
Otherwise, recursively check both left and right subtrees
Code with Comments
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case 1: Both nodes are None (empty trees or reached leaf)
        if not p and not q:
            return True
        
        # Base case 2: One node is None but the other isn't (structure mismatch)
        if not p or not q:
            return False
        
        # Base case 3: Both nodes exist but have different values
        if p.val != q.val:
            return False
        
        # Recursive case: Check both subtrees
        # Both left subtrees AND both right subtrees must be identical
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

'''Complexity Analysis
Time Complexity: O(n) where n is the number of nodes in the smaller tree (we visit each node once)
Space Complexity: O(h) where h is the height of the tree (due to recursion stack)
Example Walkthrough
For p = [1,2,3] and q = [1,2,3]:

Compare root nodes: both are 1 → continue
Compare left children: both are 2 → continue
Compare right children: both are 3 → continue
All comparisons pass → return True
For p = [4,7] and q = [4,null,7]:

Compare roots: both are 4 → continue
Compare left children: p.left = 7, q.left = None → structure mismatch → return False
The solution efficiently handles all cases by checking structure and values at each step of the recursion.'''