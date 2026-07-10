class myStack:
    
    def __init__(self, n):
        self.array = []
        self.capacity = n
    
    def isEmpty(self):
        return not self.array
    
    def isFull(self):
        return len(self.array) == self.capacity
    
    def push(self, x):
        if self.isFull():
            return
        self.array.append(x)
    
    def pop(self):
        if self.array:
            self.array.pop()
        else: return -1 
    
    def peek(self):
        return self.array[-1] if self.array else -1
        