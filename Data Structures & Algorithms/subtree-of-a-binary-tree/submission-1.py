# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
Approach Explanation
We need to check if subRoot is a subtree of root. The key insight is:

A subtree must match exactly in structure and values
We need to check every node in root as a potential starting point
Strategy:
Base cases:

If subRoot is empty, it's always a subtree (empty tree is subtree of any tree)
If root is empty but subRoot isn't, it's not a subtree
Recursive check:

At each node in root, check if the tree starting from that node is identical to subRoot
If not, recursively check the left and right subtrees
Helper function: We need a function to check if two trees are identical (same structure and values)

Time & Space Complexity:
Time: O(m × n) where m = nodes in root, n = nodes in subRoot
In worst case, we check every node in root and for each, potentially compare all nodes in subRoot
Space: O(min(m, n)) for the recursion stack depth
Code with Detailed Comments
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Main function to check if subRoot is a subtree of root.
        
        Args:
            root: The main tree
            subRoot: The potential subtree
            
        Returns:
            True if subRoot is a subtree of root, False otherwise
        """
        
        # Base case 1: Empty subtree is always a subtree of any tree
        if not subRoot:
            return True
            
        # Base case 2: If main tree is empty but subtree isn't, it's not a subtree
        if not root:
            return False
            
        # Check if trees starting from current root node are identical
        if self.isSameTree(root, subRoot):
            return True
            
        # If not identical, recursively check left and right subtrees
        # Return True if subRoot is found in either left or right subtree
        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot))
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Helper function to check if two trees are identical.
        
        Args:
            p: First tree
            q: Second tree
            
        Returns:
            True if both trees have same structure and values, False otherwise
        """
        
        # Both trees are empty - they're identical
        if not p and not q:
            return True
            
        # One tree is empty, the other isn't - not identical
        if not p or not q:
            return False
            
        # Check current node values match
        if p.val != q.val:
            return False
            
        # Recursively check left and right subtrees
        # Both must match for trees to be identical
        return (self.isSameTree(p.left, q.left) and 
                self.isSameTree(p.right, q.right))
'''How It Works - Step by Step
Let's trace through Example 1:

root = [1,2,3,4,5], subRoot = [2,4,5]
Start at root node 1

isSameTree(1, 2) returns False (values don't match)
Recursively check left subtree: isSubtree(2, 2)
At node 2 in root:

isSameTree(2, 2) returns True (check continues recursively)
Check left: isSameTree(4, 4) returns True
Check right: isSameTree(5, 5) returns True
All checks pass, so return True
Alternative Approach (Serialization)
There's also an approach using tree serialization (converting trees to strings) and checking if the serialized subRoot is a substring of serialized root. This can be more efficient in some cases but requires careful delimiter handling to avoid false matches.
'''