'''Graph Validity - Tree Problem Explained
Problem Understanding
You need to determine if a set of edges forms a valid tree. A tree has two key properties:

Connected: All nodes must be reachable from any starting node
No cycles: There should be no circular paths
For n nodes, a valid tree must have exactly n-1 edges. If you have more edges, there's a cycle. If you have fewer, it's not connected.

Approach
We'll use Depth-First Search (DFS) with cycle detection:

Build an adjacency list from the edges
Start DFS from node 0
During DFS, track visited nodes and the previous node (to avoid counting the edge we came from as a cycle)
If we revisit a node that isn't our parent, we found a cycle
Finally, check if all nodes were visited (graph is connected)
Commented Solution
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Edge case: single node is always a valid tree
        if not n:
            return True
        
        # Build adjacency list: map each node to its neighbors
        # Example: {0: [1, 2], 1: [0, 4], ...}
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)  # undirected graph - add both directions

        # Track all visited nodes to check if graph is connected
        visit = set()

        def dfs(i: int, prev: int) -> bool:
            """
            Performs DFS to detect cycles.
            
            Args:
                i: current node
                prev: parent node (the node we came from)
            
            Returns:
                False if a cycle is detected, True otherwise
            """
            # If we've already visited this node and it's not our parent, 
            # we found a cycle!
            if i in visit:
                return False

            # Mark current node as visited
            visit.add(i)
            
            # Explore all neighbors
            for j in adj[i]:
                # Skip the edge we came from (don't go back to parent)
                if j == prev:
                    continue
                
                # If DFS on neighbor returns False, cycle detected
                if not dfs(j, i):
                    return False
            
            # No cycle found in this subtree
            return True

        # Two conditions for a valid tree:
        # 1. dfs(0, -1) returns True - no cycles detected
        # 2. n == len(visit) - all nodes are connected
        return dfs(0, -1) and n == len(visit)
'''
Example Walkthrough
Example 1: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]

Adjacency list: {0: [1,2,3], 1: [0,4], 2: [0], 3: [0], 4: [1]}
DFS from 0: visits 0 → 1 → 4, then backtracks to 0 → 2, 0 → 3
All 5 nodes visited, no cycles → True ✓
Example 2: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]

There's an edge between 2-3 and 1-3, creating a cycle
When DFS reaches node 3 from node 2, it can also reach node 1 (not just through 2)
This revisit of node 1 (not the parent) signals a cycle → False ✓
Complexity
Time: O(n + e) where e is the number of edges (visit each node and edge once)
Space: O(n) for the adjacency list and visited set
'''