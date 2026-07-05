class Solution:
    def graphColoring(self, V, edges, m):
        # code here
        n = len(edges)
        
        adj = [[] for _ in range(V)]
        
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        
        color = [0] *V
        
        def isSafe(node, c):
            for a in adj[node]:
                if color[a] == c:
                    return False
            return True
        
        def recursion(node):
            if node ==V:
                return True
            
            for c in range(1, m+1):
                if isSafe(node, c):
                    color[node] = c
                    if recursion(node+1):
                        return True
                    color[node] = 0
            return False
        
        return recursion(0)