'''Clone Graph Problem Explanation
What's Being Asked?
You need to create a deep copy of an undirected graph. This means:

Every node in the original graph gets a new corresponding node
The new nodes have the same values and connections as the original
The new graph is completely independent (changing it won't affect the original)
Key Challenges
Cycles: Graphs can have cycles (node A → node B → node A). If you recursively copy without tracking, you'll get infinite loops.
Shared references: Multiple nodes might point to the same neighbor. You need to ensure you don't create duplicate copies.
The Approach: DFS with Memoization
The solution uses Depth-First Search (DFS) with a HashMap to track which nodes we've already copied:

Memoization map (oldToNew): Maps original nodes → their copies
Before copying a node's neighbors, check if it's already been copied
If yes, reuse the existing copy (prevents duplicates and breaks cycles)
If no, create a new copy and recursively copy its neighbors
Commented Solution
'''
"""
# Definition for a Node.

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Map to store original node -> cloned node
        oldToNew = {}

        def dfs(node):
            # Base case: if we've already cloned this node, return the clone
            if node in oldToNew:
                return oldToNew[node]

            # Create a new node with the same value
            copy = Node(node.val)
            
            # Add to map BEFORE processing neighbors
            # (prevents infinite loops if there are cycles)
            oldToNew[node] = copy
            
            # Recursively clone all neighbors
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        # Handle edge case: if input is None (empty graph)
        return dfs(node) if node else None
'''
Why Add to Map Before Processing Neighbors?
This is crucial for handling cycles:

If A → B → A (cycle):
  - Visit A, create copyA, add to map
  - Visit B, create copyB, add to map
  - Visit A again from B
    → Find A already in map, return copyA (no infinite loop!)
Complexity Analysis
Time: O(N + E) where N = nodes, E = edges (visit each once)
Space: O(N) for the memoization map + recursion stack
Example Walkthrough
For [[2],[1,3],[2]] (nodes: 1→2, 2→1,3, 3→2):

Start at node 1, create copy1
Process neighbor 2 → create copy2
Process neighbor 1 of node 2 → already exists! Return copy1
Process neighbor 3 → create copy3
Process neighbor 2 of node 3 → already exists! Return copy2
Result: A properly cloned graph with correct connections.
'''