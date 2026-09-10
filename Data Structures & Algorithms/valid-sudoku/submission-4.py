class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        row,col = 0,0
        for col in range(0,9):
            xset = set()
            for row in range(0,9):
                if board[row][col] in xset and board[row][col] != '.':
                    return False
                else:
                    xset.add(board[row][col])
        row,col = 0,0
        for row in range(0,9):
            yset = set()
            for col in range(0,9):
                if board[row][col] in yset and board[row][col] != '.':
                    return False
                else:
                    yset.add(board[row][col])

        rotr, rotc = 0,0
        row,col = 0,0
        for rotr in range(0,9,3):
            for rotc in range(0,9,3):
                ssud = set()    
                for row in range(0,3):
                    for col in range(0,3):
                        if board[row+rotr][col+rotc] in ssud and board[row+rotr][col+rotc] != ".":
                            return False
                        else:
                            ssud.add(board[row+rotr][col+rotc])
        
        return True



                

        #return True
        
        '''
        i = 0
        j = 0
        length = len(board)
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == board[i][j+1] and j < length:
                    return False
        for j in range(len(board)):
            for i in range(len(board)):
                if board[i][j] == board[i+1][j] and i < length:
                    return False
        return True
'''
        
        



