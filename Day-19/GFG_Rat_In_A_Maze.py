class Solution:
    def ratInMaze(self, maze):
        n = len(maze)
        if maze[0][0] == 0 or maze[n-1][n-1] == 0:
            return []
            
        ans = []
        visited = [[0]*n for _ in range(n)]
        
        direction = [[1, 0, 'D'], [0, -1, 'L'], [0, 1, 'R'], [-1, 0, 'U']]
        
        def recursion(r, c, path):
            if r == n-1 and c == n-1:
                ans.append(path)
                return
            visited[r][c] = 1
            
            for dr,dc, di in direction:
                nr, nc = r+ dr, c+ dc
                if 0 <= nr<n and 0 <= nc < n and maze[nr][nc] and not visited[nr][nc]:
                    recursion(nr, nc, path+di)
            visited[r][c] = 0
        
        recursion(0, 0, "")
        
        return ans