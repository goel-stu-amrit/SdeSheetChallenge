class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = ["."*n for _ in range(n)]
        ans = []
        leftRow = [0]*n
        upprDiag = [0]*(2*n-1)
        lowerDiag = [0]*(2*n-1)
        def recursion(col):
            if col == n:
                ans.append(board[:])
                return
            for i in range(n):
                if leftRow[i] == 0 and upprDiag[n-1+col-i] ==0 and lowerDiag[i+col] ==0 :
                    board[i] = board[i][:col] + "Q"+ board[i][col+1:]
                    leftRow[i], upprDiag[n-1+col-i], lowerDiag[i+col] = 1, 1, 1
                    recursion(col+1)
                    board[i] = board[i][:col] + "."+ board[i][col+1:]
                    leftRow[i], upprDiag[n-1+col-i], lowerDiag[i+col]  = 0, 0, 0
        recursion(0)
        return ans
        