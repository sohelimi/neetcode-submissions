'''Understanding the Problem
We need to reconstruct a binary tree from two traversal arrays:

Preorder: Root → Left subtree → Right subtree
Inorder: Left subtree → Root → Right subtree
The key insight is that in preorder, the first element is always the root. We can then find this root in the inorder array to determine which elements belong to the left and right subtrees.

Approach
Base case: If either array is empty, return None
Root identification: The first element in preorder is the root
Find root in inorder: Locate the root's position in inorder array
Split arrays:
Left subtree: elements before root in inorder
Right subtree: elements after root in inorder
Recursive construction:
Build left subtree with corresponding portions of both arrays
Build right subtree with corresponding portions of both arrays
Code Implementation
'''
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Reconstruct binary tree from preorder and inorder traversals.
        
        Args:
            preorder: List[int] - Preorder traversal of the tree
            inorder: List[int] - Inorder traversal of the tree
            
        Returns:
            TreeNode: Root of the reconstructed binary tree
        """
        # Base case: if either array is empty, return None
        if not preorder or not inorder:
            return None
        
        # First element in preorder is always the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Find the position of root in inorder array
        # This splits the tree into left and right subtrees
        mid = inorder.index(root_val)
        
        # Recursively build left subtree:
        # - preorder[1:mid+1]: First 'mid' elements after root (size of left subtree)
        # - inorder[:mid]: All elements before root in inorder (left subtree)
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        
        # Recursively build right subtree:
        # - preorder[mid+1:]: Remaining elements after left subtree
        # - inorder[mid+1:]: All elements after root in inorder (right subtree)
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root

'''
Example Walkthrough
For preorder = [1,2,3,4] and inorder = [2,1,3,4]:

Root = 1 (first element of preorder)
Find 1 in inorder: position 1
Left subtree:
Inorder: [2] (elements before 1)
Preorder: [2] (next 1 element after root)
Right subtree:
Inorder: [3,4] (elements after 1)
Preorder: [3,4] (remaining elements)
Recursively build subtrees
Complexity Analysis
Time Complexity: O(n²) in worst case due to index() search for each node
Can be optimized to O(n) using a hashmap to store value-index pairs
Space Complexity: O(n) for recursion stack and new tree nodes
Key Points to Remember
Preorder always gives the root first
Inorder tells us what's in left vs right subtrees
The size of left subtree in preorder = number of elements before root in inorder
All values are unique, so we can safely use index()
'''        