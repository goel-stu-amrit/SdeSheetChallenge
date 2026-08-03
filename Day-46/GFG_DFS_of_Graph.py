class Solution:
    def dfs(self, adj):
        n = len(adj)
        visited = [0]*n
        ans = []
        def recursion(node) :
            visited[node] = 1
            ans.append(node)
            
            for nei in adj[node]:
                if not visited[nei]:
                    recursion(nei)
                    
        recursion(0)
        return ans