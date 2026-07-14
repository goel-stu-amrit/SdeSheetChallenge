class Solution:
    def celebrity(self, mat):
        n=len(mat)
        if n == 1 : return 0
        top, down = 0, n-1
        while top < down:
            if mat[top][down] == 1:
                top+=1
            elif mat[down][top] == 1:
                down-=1
            else :
                top+=1
                down-=1
        if top > down:
            return -1
        for i in range(n):
            if top == i:
                continue
            if mat[top][i] == 0 and mat[i][top] == 1:
                continue
            else:
                return -1
        return top