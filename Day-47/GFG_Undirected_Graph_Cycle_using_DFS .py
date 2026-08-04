class Solution:
    # Detect A cycle in Undirected Graph using DFS 
	def isCycle(self, V, edges):
	    adj = [[] for _ in range(V)]
	    for u,v in edges:
	        adj[u].append(v)
	        adj[v].append(u)
		visited = [False]*V
		
		for i in range(V):
		    if not visited[i]:
		        stack = [(i, -1)]
		        visited[i] = True
		        while stack:
		            node, parent = stack.pop()
		            for nei in adj[node]:
		                if not visited[nei]:
		                    visited[nei] = True
		                    stack.append((nei, node))
		                elif nei != parent:
		                    return True
	    return False