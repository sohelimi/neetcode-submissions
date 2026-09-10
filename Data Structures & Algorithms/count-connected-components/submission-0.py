'''Connected Components Problem Explanation
What's the Problem?
You have an undirected graph with n nodes (0 to n-1) and a list of edges connecting pairs of nodes. A connected component is a group of nodes where every node can reach every other node in that group through edges.

Your task: Count how many separate connected components exist.

Visual Example
Example 1: n=5, edges=[[0,1],[1,2],[3,4]]

Component 1: 0 — 1 — 2
Component 2: 3 — 4
Isolated: 

Answer: 2 components
Approach: Union-Find (Disjoint Set Union)
The most elegant solution uses Union-Find, which efficiently groups connected nodes:

Union: When we see an edge between nodes a and b, we merge them into the same component
Find: After processing all edges, we find the parent/root of each node
Count: The number of unique parents = number of components
Here's the completed code with comments:
'''
class UnionFind:
    def __init__(self):
        # Dictionary to store parent relationships
        # Initially, each node is its own parent
        self.f = {}
    
    def findParent(self, x: int) -> int:
        # Find the root parent of node x with path compression
        # Path compression: connect nodes directly to root for faster future lookups
        y = self.f.get(x, x)  # Get parent, or x itself if not in dict
        if x != y:
            # Recursively find and store the root
            y = self.f[x] = self.findParent(y)
        return y
    
    def union(self, x: int, y: int):
        # Merge two nodes by connecting their root parents
        # Find roots of both nodes and make one the parent of the other
        self.f[self.findParent(x)] = self.findParent(y)

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Initialize Union-Find data structure
        dsu = UnionFind()
        
        # Process each edge by unioning the two connected nodes
        for a, b in edges:
            dsu.union(a, b)
        
        # Count unique parents (components)
        # For each node 0 to n-1, find its root parent
        # The number of unique roots = number of components
        return len(set(dsu.findParent(x) for x in range(n)))
'''
Complexity Analysis
Time: O(n + e × α(n)) where e is edges and α is inverse Ackermann (nearly constant)
Space: O(n) for the Union-Find structure
Why This Works
After all unions, nodes in the same component share the same root parent. By finding all unique roots, we count distinct components.

Key insight: We must check ALL nodes (0 to n-1), not just those in edges, to catch isolated nodes that have no edges!
'''