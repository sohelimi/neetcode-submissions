# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
A valid BST requires that for every node:

All nodes in its left subtree must have values less than the node's value.
All nodes in its right subtree must have values greater than the node's value.
The key insight is that we need to track allowed ranges for each node's value as we traverse the tree.

Approach
We can use DFS (Depth-First Search) with range checking:

Start with the root node having an allowed range of (-∞, ∞)
For each node:
Check if its value is within the current allowed range
Recursively check left child with updated range: (current_min, node.val)
Recursively check right child with updated range: (node.val, current_max)
Time & Space Complexity
Time: O(n) where n is the number of nodes (we visit each node once)
Space: O(h) where h is the height of the tree (recursion stack)

'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Helper function to validate a subtree
        def validate(node, min_val, max_val):
            """
            Validate if the subtree rooted at 'node' is a valid BST.
            
            Args:
                node: Current node being checked
                min_val: Minimum allowed value for this node (exclusive)
                max_val: Maximum allowed value for this node (exclusive)
            
            Returns:
                True if valid BST, False otherwise
            """
            # Base case: empty node is always valid
            if not node:
                return True
            
            # Check if current node's value violates BST property
            # Node value must be strictly between min_val and max_val
            if not (min_val < node.val < max_val):
                return False
            
            # Recursively validate left and right subtrees with updated ranges:
            # - Left subtree: all values must be less than current node's value
            # - Right subtree: all values must be greater than current node's value
            return (validate(node.left, min_val, node.val) and 
                    validate(node.right, node.val, max_val))
        
        # Start validation from root with initial range of (-∞, ∞)
        return validate(root, float('-inf'), float('inf'))

'''
Key Points in the Code:
Range Tracking: Each recursive call carries the allowed range for node values.
Exclusive Boundaries: We use < not ≤ because BST requires strict inequality.
Base Case: An empty node (None) is trivially a valid BST.
Initial Range: We start with (-∞, ∞) since the root has no constraints.
Example Walkthrough:
For root = [2,1,3]:

Root (2): Check -∞ < 2 < ∞ → True
Left child (1): Check -∞ < 1 < 2 → True
Right child (3): Check 2 < 3 < ∞ → True
Result: True
For root = [1,2,3]:

Root (1): Check -∞ < 1 < ∞ → True
Left child (2): Check -∞ < 2 < 1 → False (violation!)
Result: False
This approach efficiently validates the entire tree in one pass while maintaining the BST properties.
'''        