'''Problem Explanation
Let me break down this problem step by step:

The Setup
You have a 2D grid where each cell has a height
Pacific Ocean borders the top and left edges
Atlantic Ocean borders the bottom and right edges
Water flows from higher cells to equal or lower cells (in 4 directions)
The Goal
Find all cells where water can reach both oceans.

Key Insight
Instead of asking "from each cell, can water reach both oceans?" (hard), we flip the question:

"Which cells can receive water from the Pacific border?"
"Which cells can receive water from the Atlantic border?"
The answer is cells in both sets!
This works because water can flow both directions in terms of reachability - if water flows down a mountain, we can trace backward up the mountain.

Algorithm
DFS from Pacific border (top and left edges) - mark all cells reachable from Pacific
DFS from Atlantic border (bottom and right edges) - mark all cells reachable from Atlantic
Find intersection - cells in both sets are the answer
Completed Code with Comments
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        
        # Sets to store cells that can reach Pacific and Atlantic respectively
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            """
            DFS helper function to explore reachable cells from a border.
            
            Args:
                r, c: current row and column
                visit: set of visited cells for this ocean
                prevHeight: the height of the previous cell we came from
            """
            # Base cases: out of bounds, already visited, or height is too low
            # (water can only flow to equal or lower heights)
            if (
                (r, c) in visit
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            
            # Mark this cell as visited for the current ocean
            visit.add((r, c))
            
            # Explore all 4 directions: down, up, right, left
            dfs(r + 1, c, visit, heights[r][c])  # down
            dfs(r - 1, c, visit, heights[r][c])  # up
            dfs(r, c + 1, visit, heights[r][c])  # right
            dfs(r, c - 1, visit, heights[r][c])  # left

        # Start DFS from all Pacific border cells (top and left edges)
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])  # top row
        
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])  # left column

        # Start DFS from all Atlantic border cells (bottom and right edges)
        for c in range(COLS):
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])  # bottom row
        
        for r in range(ROWS):
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])  # right column

        # Collect all cells that can reach both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        
        return res
'''
Complexity Analysis
Time: O(rows × cols) - each cell is visited once per ocean search
Space: O(rows × cols) - for the visited sets and recursion stack
'''