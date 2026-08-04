class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(n)]
        
        queue = []
        indegree = [0]* n
        
        for i, j in prerequisites:
            indegree[j] +=1
            adj[i].append(j)

        for i in range(n):
            if indegree[i] == 0 : queue.append(i)

        start = 0
        topo = []
        
        while start<len(queue):
            node = queue[start]
            start+=1
            topo.append(node)
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i] ==0 : queue.append(i)

        return True if len(topo) == n else False
