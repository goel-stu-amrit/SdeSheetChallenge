class Solution:
    def topKSumPairs(self, a, b, k):
        a.sort()
        b.sort()
        n = len(a) 
        hq = [(-(a[-1]+b[-1]),n-1,n-1)]
        visited = set()
        visited.add((n-1,n-1))
        ans = []
        while len(ans) < k:
            val, i, j = heapq.heappop(hq)
            ans.append(-val)
            if i > 0  and (i-1,j) not in visited:
                heapq.heappush(hq, (-(a[i-1]+ b[j]), i-1, j))
                visited.add((i-1, j))
            if j>0 and (i, j-1) not in visited:
                heapq.heappush(hq, (-(a[i]+ b[j-1]), i, j-1))
                visited.add((i, j-1))
        return ans