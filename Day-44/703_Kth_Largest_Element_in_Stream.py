class KthLargest(object):
    def __init__(self, k, nums):
        self.k = k
        self.hq = []
        for i in nums:
            if len(self.hq) < self.k: heapq.heappush(self.hq, i)
            elif i > self.hq[0]:
                heapq.heappop(self.hq)
                heapq.heappush(self.hq, i)

    def add(self, val):
        if len(self.hq) < self.k: heapq.heappush(self.hq, val)
        elif val > self.hq[0]:
            heapq.heappop(self.hq)
            heapq.heappush(self.hq, val)
        return self.hq[0]