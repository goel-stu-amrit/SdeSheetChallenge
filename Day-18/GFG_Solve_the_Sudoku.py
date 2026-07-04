class Solution:
    def solveSudoku(self, board):
        # code here
        def isValid(i,j,k):
            for m in range(9):
                if board[i][m] == k: return False
                if board[m][j] == k: return False
                row = (i//3)*3 + m//3
                col = 3*(j//3) + m%3
                if board[row][col] == k: return False
            return True 

        def recursion():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == 0:
                        for c in range(1,10):
                            if isValid(i,j,c):
                                board[i][j] = c
                                if recursion(): return True
                                board[i][j] = 0
                        return False
            return True
        recursion()