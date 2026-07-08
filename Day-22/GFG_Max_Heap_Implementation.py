class maxHeap:

    def __init__(self):
        self.hq = []
        
    def push(self, x: int):
        heapq.heappush(self.hq, -x)

    def pop(self):
        heapq.heappop(self.hq)

    def peek(self) -> int:
        if not self.hq: return -1
        return -self.hq[0]

    def size(self) -> int:
        return len(self.hq)