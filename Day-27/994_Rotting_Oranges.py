class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j, 0))
                elif grid[i][j] == 1:
                    fresh+=1
        if fresh == 0: return 0
        start, count, time = 0, 0, 0
        while(start < len(q)):
            r, c, t = q[start]
            start+=1
            time = max(time, t)
            for dr, dc in [[0,1], [1,0], [0,-1], [-1,0]]:
                nr, nc = r+dr, c+dc
                if 0<= nr <m and 0<= nc<n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc, t+1))
                    count+=1
        return time if count==fresh else -1