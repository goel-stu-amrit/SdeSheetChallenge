from collections import deque
class Solution:
    def isBipartite(self, graph): # Using BFS
        n = len(graph)
        colour = [-1]*n
        for i in range(n):
            if colour[i] != -1:
                continue
            queue = deque([i])
            colour[i] = 1
            while queue:
                node = queue.popleft()
                for nei in graph[node]:
                    if colour[nei] == -1:
                        colour[nei] = 1-colour[node]
                        queue.append(nei)
                    elif colour[nei] == colour[node] :
                        return False
        return True