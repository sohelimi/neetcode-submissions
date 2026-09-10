# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        
        def inorder(node):
            if not node or self.result is not None:
                return
            
            inorder(node.left)      # Visit left subtree
            
            self.k -= 1             # Process current node
            if self.k == 0:
                self.result = node.val
                return
            
            inorder(node.right)     # Visit right subtree
        
        inorder(root)
        return self.result