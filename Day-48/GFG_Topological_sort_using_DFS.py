class Solution:
    def topoSort(self, V: int, edges: list[list[int]]) -> list[int]:
        #Topological sort using DFS
        visited = [0]* V
        adj = [[] for _ in range(V)]
        for i, j in edges:
            adj[i].append(j)
        stack = []
        def dfs(node):
            visited[node] = 1
            for nei in adj[node]:
                if not visited[nei]:
                    dfs(nei)
            stack.append(node)
        for i in range(V):
            if not visited[i]:
                dfs(i)
                
        return stack[::-1]