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

'''
Step-by-Step Walkthrough
Let's trace through the algorithm with a simple example:

    3
   / \
  1   4
   \
    2
Finding 2nd smallest (k=2):

Start at root (3), push to stack: [3]
Go left to 1, push to stack: [3, 1]
1 has no left child, so pop from stack: curr = 1, k = 2-1 = 1
k ≠ 0, so move to right child of 1 (which is 2)
Push 2 to stack: [3, 2]
2 has no left child, so pop from stack: curr = 2, k = 1-1 = 0
k = 0, return 2 ✅
Time & Space Complexity
Time Complexity: O(h + k) where h is the height of the tree

In worst case (skewed tree): O(n)
In balanced tree: O(log n + k)
Space Complexity: O(h) for the stack

In worst case (skewed tree): O(n)
In balanced tree: O(log n)
'''        