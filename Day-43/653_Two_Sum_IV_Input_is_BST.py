class BstIter():
    def __init__(self, root, isreverse):
        self.stack = []
        self.reverse = isreverse
        self.pushAll(root)

    def pushAll(self, node):
        while node:
            self.stack.append(node)
            node = node.right if self.reverse else node.left
    
    def next(self):
        node = self.stack.pop()
        if self.reverse: self.pushAll(node.left)
        else: self.pushAll(node.right)
        return node.val

class Solution(object):
    def findTarget(self, root, k):
        if not root: return False
        l = BstIter(root, False)
        r = BstIter(root, True)
        i = l.next()
        j = r.next()
        while i<j:
            if i+j== k: return True
            elif i+j > k: j = r.next()
            else: i = l.next()
        return False

