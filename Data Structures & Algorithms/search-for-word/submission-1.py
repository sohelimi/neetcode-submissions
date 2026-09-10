class Solution:
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get number of rows and columns in the board
        rows, cols = len(board), len(board[0])

        # DFS function to explore the board
        def dfs(r, c, i):
            # r = current row
            # c = current column
            # i = current index in the word
            
            # ✅ BASE CASE:
            # If we've matched all characters in the word
            if i==len(word):
                return True #Word found
            # ❌ INVALID CONDITIONS:
            # - Out of bounds
            # - Character does not match
            if (r < 0 or r >= rows or
                c < 0 or cols >= cols or
                board[r][c] != word[i]):
                return False
            
             # 🔒 MARK VISITED:
            # Save current value before overwriting
            temp = board[r][c]

            # Mark the cell as visited so we don't reuse it
            board[r][c] = "#"

            # 🔄 EXPLORE ALL 4 DIRECTIONS:
            found = (
                dfs(r+1, c, i+1) or #go down
                dfs(r-1, c, i+1) or #go Up
                dfs(r, c+1, i+1) or #go right
                dfs(r, c-1, i+1) #go left
            )

            # 🔁 BACKTRACK:
            # Restore the original value after exploring
            board[r][c] = temp

            # Return whether we found the word from this path
            return found

        # 🚀 TRY EVERY CELL AS STARTING POINT
        for r in range(rows):
            for c in range(cols):
                 # Start DFS from each cell
                if dfs(r,c,0):
                    return True # Word found
        # If no path matches the word
        return False  
        '''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        # Get number of rows and columns in the board
        rows, cols = len(board), len(board[0])

        # DFS function to explore the board
        def dfs(r, c, i):
            # r = current row
            # c = current column
            # i = current index in the word
            
            # ✅ BASE CASE:
            # If we've matched all characters in the word
            if i == len(word):
                return True  # Word found
            
            # ❌ INVALID CONDITIONS:
            # - Out of bounds
            # - Character does not match
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                board[r][c] != word[i]):
                return False
            
            # 🔒 MARK VISITED:
            # Save current value before overwriting
            temp = board[r][c]
            
            # Mark the cell as visited so we don't reuse it
            board[r][c] = "#"
            
            # 🔄 EXPLORE ALL 4 DIRECTIONS:
            found = (
                dfs(r + 1, c, i + 1) or   # go DOWN
                dfs(r - 1, c, i + 1) or   # go UP
                dfs(r, c + 1, i + 1) or   # go RIGHT
                dfs(r, c - 1, i + 1)      # go LEFT
            )
            
            # 🔁 BACKTRACK:
            # Restore the original value after exploring
            board[r][c] = temp
            
            # Return whether we found the word from this path
            return found

        # 🚀 TRY EVERY CELL AS STARTING POINT
        for r in range(rows):
            for c in range(cols):
                
                # Start DFS from each cell
                if dfs(r, c, 0):
                    return True  # Word found
        
        # If no path matches the word
        return False  