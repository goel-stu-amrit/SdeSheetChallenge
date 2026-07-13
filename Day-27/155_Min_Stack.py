class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if self.stack:
            mn = self.stack[-1][1]
            if val < mn:
                self.stack.append([val, val])
            else:
                self.stack.append([val, mn])
        else:
            self.stack.append([val, val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None
)