'''Number of Islands - Problem Explanation
What's the problem asking?
You have a 2D grid where:

'1' = land
'0' = water
An island is a group of connected '1's (connected horizontally or vertically, not diagonally). Your goal is to count how many separate islands exist.

Think of it like: if you have a map with multiple landmasses, how many distinct landmasses are there?

Key Insight
Every time you find a '1' that hasn't been visited yet, it's either a new island or part of an island you haven't explored. So:

Scan the entire grid
When you find an unvisited '1', increment island count
Explore all connected '1's from that cell (mark them as visited)
Continue scanning
Approach: Depth-First Search (DFS)
When you find a new '1', use DFS to explore all connected lands and mark them as visited. This way, when you encounter those cells again, you won't count them as new islands.

Complete Code with Comments
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: empty grid
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()  # Track visited cells to avoid revisiting
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            """
            Explore all connected lands from position (r, c) using DFS.
            Mark each visited cell to avoid reprocessing.
            """
            # Base cases: out of bounds, water, or already visited
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            # Mark current cell as visited
            visit.add((r, c))

            # Explore all 4 adjacent directions: right, left, down, up
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Scan entire grid
        for r in range(rows):
            for c in range(cols):
                # Found an unvisited land cell
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1  # New island found
                    dfs(r, c)  # Explore all connected lands
        
        return islands
'''
Complexity Analysis
Time: O(rows × cols) - visit each cell at most once
Space: O(rows × cols) - visit set stores all cells in worst case, + recursion stack can go up to O(rows × cols) in a single island
Example Walkthrough
For grid:

["1","1","0"]
["0","1","0"]
["1","0","1"]
Start at (0,0), find '1' → islands = 1, DFS explores (0,0)→(0,1)→(1,1)
Continue scanning → find (2,0) '1' → islands = 2, DFS explores (2,0)
Continue scanning → find (2,2) '1' → islands = 3, DFS explores (2,2)
Result: 3 islands
'''