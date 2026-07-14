class StockSpanner:
    def __init__(self):
        self.stack = []
        self.count = 0
    def next(self, price: int) -> int:
        self.count+=1
        if self.stack and self.stack[-1][0] > price:
            self.stack.append([price, self.count])
            return 1
        if not self.stack:
            self.stack.append([price, self.count])
            return 1
        while self.stack and self.stack[-1][0] <= price:
            self.stack.pop()
        if not self.stack :
            self.stack.append([price, self.count])
            return self.count
        self.stack.append([price, self.count])
        return self.count - self.stack[-2][1]