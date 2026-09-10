# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
Understanding Level Order Traversal
Level order traversal visits nodes level by level from top to bottom, left to right. For the example tree:

      1
     / \
    2   3
   / \ / \
  4  5 6  7
The traversal would be: Level 0: [1], Level 1: [2, 3], Level 2: [4, 5, 6, 7]

Approach
We use a queue (FIFO - First In First Out) to process nodes:

Start with the root node in the queue
While the queue is not empty:
Process all nodes at the current level (current queue size)
For each node: add its value to the current level's list
Add its children (left then right) to the queue for the next level
Append the current level's list to the result


from collections import deque
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize result list to store levels
        result = []
        
        # Use deque for efficient pop from left (queue operations)
        queue = deque()
        
        # If tree is not empty, start with root
        if root:
            queue.append(root)
        
        # Process while there are nodes in the queue
        while queue:
            # List to store values at current level
            level_values = []
            
            # Number of nodes at current level
            level_size = len(queue)
            
            # Process all nodes at current level
            for _ in range(level_size):
                # Get the next node from front of queue
                node = queue.popleft()
                
                # Add node's value to current level list
                level_values.append(node.val)
                
                # Add children to queue for next level (if they exist)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Add current level's values to result
            result.append(level_values)
'''
from collections import deque

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val        # value of node
        self.left = left      # left child
        self.right = right    # right child


class Solution:
    def levelOrder(self, root):
        # If tree is empty → return empty list
        if not root:
            return []

        result = []                  # Final answer
        queue = deque([root])        # Queue for BFS (start with root)

        # Continue until queue is empty
        while queue:
            level_size = len(queue)  # Number of nodes in current level
            level = []               # Store values of this level

            # Process ALL nodes in current level
            for _ in range(level_size):
                node = queue.popleft()   # Remove from front of queue
                
                # Add node value to current level
                level.append(node.val)

                # Add children to queue for next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add completed level to result
            result.append(level)

        return result        