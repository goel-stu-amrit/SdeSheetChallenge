class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addFront(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.size += 1

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def removeLast(self):
        if self.size == 0: return None
        node = self.tail.prev
        self.remove(node)
        return node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0
        self.keyMap = {}
        self.freqMap = {}

    def updateFreq(self, node):
        freq = node.freq
        dll = self.freqMap[freq]
        dll.remove(node)
        if dll.size == 0:
            del self.freqMap[freq]
            if self.minFreq == freq:
                self.minFreq += 1
        node.freq += 1
        if node.freq not in self.freqMap:
            self.freqMap[node.freq] = DoublyLinkedList()
        self.freqMap[node.freq].addFront(node)

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1
        node = self.keyMap[key]
        self.updateFreq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0: return
        if key in self.keyMap:
            node = self.keyMap[key]
            node.value = value
            self.updateFreq(node)
            return
        if len(self.keyMap) == self.capacity:
            dll = self.freqMap[self.minFreq]
            node = dll.removeLast()
            del self.keyMap[node.key]
            if dll.size == 0:
                del self.freqMap[self.minFreq]
        node = Node(key, value)
        self.minFreq = 1
        if 1 not in self.freqMap:
            self.freqMap[1] = DoublyLinkedList()
        self.freqMap[1].addFront(node)
        self.keyMap[key] = node