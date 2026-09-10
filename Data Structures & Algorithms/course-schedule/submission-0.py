'''Course Schedule Problem Explanation
This is a cycle detection problem disguised as a course scheduling question. Let me break it down:

Problem Core Concept
You need to determine if you can complete all courses given their prerequisites. The key insight:

If course A requires course B, and course B requires course A (directly or indirectly), you have a cycle → impossible to complete
If no cycles exist, all courses can be completed
Why It's a Graph Problem
Think of it as a directed graph:

Each course is a node
Each prerequisite creates an edge: a → b means "a depends on b"
A cycle means you're stuck in circular dependencies
Solution Approach: DFS with Cycle Detection
The reference solution uses DFS (Depth-First Search) with a visiting set to detect cycles:

Build a prerequisite map: For each course, store its prerequisites
For each course, do DFS: Try to visit all its dependencies
Track visiting state: If we revisit a course currently in our DFS path, we found a cycle!
Mark as safe: Once we verify a course has no cycles, mark it as done (clear its prerequisites)
Commented Code
'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build a map: course -> list of prerequisites
        preMap = {i: [] for i in range(numCourses)}
        
        # Populate the map with prerequisites
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        # Track courses currently in our DFS path (for cycle detection)
        visiting = set()
        
        def dfs(crs):
            # CYCLE DETECTED: we've seen this course in current path
            if crs in visiting:
                return False
            
            # BASE CASE: no prerequisites, can take this course
            if preMap[crs] == []:
                return True
            
            # Add to current path
            visiting.add(crs)
            
            # Check all prerequisites of this course
            for pre in preMap[crs]:
                # If any prerequisite leads to a cycle, return False
                if not dfs(pre):
                    return False
            
            # Remove from current path (backtrack)
            visiting.remove(crs)
            
            # OPTIMIZATION: clear prerequisites to avoid rechecking
            # (this course is safe, no cycles found)
            preMap[crs] = []
            
            return True
        
        # Check every course for cycles
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        # No cycles found, all courses can be completed
        return True
'''Example Walkthrough
Example 2: numCourses = 2, prerequisites = [[0,1],[1,0]]

preMap = {0: [1], 1: [0]}

dfs(0):
  visiting = {0}
  dfs(1):  # check prerequisite of 0
    visiting = {0, 1}
    dfs(0):  # check prerequisite of 1
      0 in visiting? YES → return False (cycle!)
Complexity Analysis
Time: O(V + E) where V = courses, E = prerequisites
We visit each course once and traverse each edge once
Space: O(V) for the recursion stack and visiting set
'''



