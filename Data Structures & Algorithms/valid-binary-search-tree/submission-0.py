# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

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