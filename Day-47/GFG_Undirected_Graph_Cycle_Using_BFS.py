from collections import deque
class Solution:
    # Detect A cycle in Undirected Graph using BFS 
	def isCycle(self, V, edges):
	    adj = [[] for _ in range(V)]
	    for u,v in edges:
	        adj[u].append(v)
	        adj[v].append(u)
		visited = [False]*V
		
		for i in range(V):
		    if not visited[i]:
		        queue = deque([(i, -1)])
		        visited[i] = True
		        while queue:
		            node, parent = queue.popleft()
		            for nei in adj[node]:
		                if not visited[nei]:
		                    visited[nei] = True
		                    queue.append((nei, node))
		                elif nei != parent:
		                    return True
	    return False