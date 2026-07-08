class Solution(object):
    def findKthLargest(self, nums, k):
        hq = []
        for i in nums:
            if len(hq) == k:
                if i > hq[0]:
                    heapq.heappop(hq)
                    heapq.heappush(hq, i)
            else:
                heapq.heappush(hq, i)
        return hq[0]
        