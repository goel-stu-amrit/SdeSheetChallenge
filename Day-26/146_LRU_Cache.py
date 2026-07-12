class Node:
    def __init__(self, key =-1, val=-1):
        self.key = key
        self.val = val 
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.n = capacity
        self.obj = {}
        self.head, self.tail = Node(), Node()
        self.head.next, self.tail.prev = self.tail, self.head
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def addInFront(self, newNode):
        newNode.next = self.head.next
        newNode.prev =  self.head
        self.head.next = newNode
        newNode.next.prev = newNode
    
    def get(self, key: int) -> int:
        if key in self.obj:
            node = self.obj[key]
            self.remove(node)
            self.addInFront(node)
            return node.val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.obj:
            node = self.obj[key]
            node.val = value
            self.remove(node)
            self.addInFront(node)
            self.obj[key] = node
            return
        if len(self.obj) == self.n:
            lru = self.tail.prev
            self.remove(lru)
            del self.obj[lru.key]
        node = Node(key, value)
        self.addInFront(node)
        self.obj[key] = node