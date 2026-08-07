from collections import deque
class Solution:
    def numIslands(self, grid):
        m,n = len(grid), len(grid[0])
        visited = [[0]*n for _ in range(m)]
        islands = 0
        def bfs(i, j):
            visited[i][j] = 1
            queue = deque([(i,j)])
            while queue:
                r, c = queue.popleft()
                for dr, dc in [[-1,0],[0,1],[1,0],[0,-1]]:
                    nr, nc = r+dr, c+dc
                    if 0<=nr< m and 0<=nc<n and grid[nr][nc] =="1" and not visited[nr][nc]:
                        visited[nr][nc] = 1
                        queue.append((nr, nc))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1" and not visited[i][j]:
                    islands+=1
                    bfs(i, j)
        return islands