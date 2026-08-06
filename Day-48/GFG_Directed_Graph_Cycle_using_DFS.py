class Solution:
    def isCyclic(self, V: int, edges: list[list[int]]) -> bool:
        # Detect A cycle in a Directed Graph using DFS
        adj = [[] for _ in range(V)]
        for i, j in edges:
            adj[i].append(j)
        visited = [0]* V
        pathVisited = [0]* V
        def dfs(node):
            visited[node] =1
            pathVisited[node] =1
            for nei in adj[node]:
                if not visited[nei]:
                    if dfs(nei): return True
                elif pathVisited[nei]:
                    return True
            
            pathVisited[node] = 0
            return False
        
        for i in range(V):
            if not visited[i]:
                if dfs(i): return True
        
        return False