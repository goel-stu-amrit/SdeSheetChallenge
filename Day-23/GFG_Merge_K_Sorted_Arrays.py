class Solution:
    def mergeArrays(self, mat):
        hq = []
        n, m = len(mat), len(mat[0])
        for i in range(n):
            heapq.heappush(hq, (mat[i][0], i, 0))
        result = []
        while len(hq):
            x,i,j = heapq.heappop(hq)
            result.append(x)
            if j < m-1:
                heapq.heappush(hq, (mat[i][j+1], i, j+1))
        return result
        