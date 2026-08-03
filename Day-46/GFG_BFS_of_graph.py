class Solution:
    def bfs(self, adj):
        n = len(adj)
        visited = [0]*n
        ans = []
        queue = deque([0])
        visited[0] = 1
        while queue:
            node = queue.popleft()
            ans.append(node)
            for i in adj[node]:
                if not visited[i]:
                    visited[i] = 1
                    queue.append(i)
        return ans