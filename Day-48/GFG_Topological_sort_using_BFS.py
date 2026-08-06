from collections import deque
class Solution:
    def topoSort(self, V: int, edges: list[list[int]]) -> list[int]:
        # Kahn's algorithm- Topological sort using BFS
        adj = [[] for _ in range(V)]
        indegree = [0]*V
        for i, j in edges:
            adj[i].append(j)
            indegree[j]+=1
        que = deque()
        for i in range(V):
            if indegree[i] ==0: que.append(i)
            
        topo = []
        while que:
            node = que.popleft()
            topo.append(node)
            for nei in adj[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    que.append(nei)
        return topo