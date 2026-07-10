class myQueue:
    def __init__(self, n):
        self.array = []
        self.capacity = n
    
    def isEmpty(self):
        return not self.array
    
    def isFull(self):
        return len(self.array) == self.capacity
    
    def enqueue(self, x):
        self.array.append(x)
    
    def dequeue(self):
        self.array.pop(0)
    
    def getFront(self):
       return self.array[0] if self.array else -1
    
    def getRear(self):
        return self.array[-1] if self.array else -1
        