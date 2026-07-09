class Solution(object):
    def topKFrequent(self, nums, k):
        obj = defaultdict(int)
        for i in nums:
            obj[i] = (obj[i] or 0) +1
        hq, result = [], []
        for i, j in obj.items():
            heapq.heappush(hq, (j,i))
            if len(hq) >k: heapq.heappop(hq)
        while hq:
            j,i = heapq.heappop(hq)
            result.append(i)
        return result