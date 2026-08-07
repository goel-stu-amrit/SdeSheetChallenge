class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool: # Using DFS
        n = len(graph)
        colour = [-1]*n
        def dfs(i, col):
            colour[i] = col
            for nei in graph[i]:
                if colour[nei] == -1 and not dfs(nei, 1-col):
                    return False
                elif colour[nei] == col: return False
            return True
        for i in range(n):
            if colour[i] == -1 and not dfs(i, 0): return False
        return True