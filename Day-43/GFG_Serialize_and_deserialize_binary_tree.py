'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def serialize(self, root):
        if not root:
            return ""
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.data))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("N")
        return ",".join(res)

    def deSerialize(self, arr):
        if not arr:
            return None
        vals = arr.split(",")
        root = Node(int(vals[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if vals[i] != "N":
                node.left = Node(int(vals[i]))
                q.append(node.left)
            i += 1
            if vals[i] != "N":
                node.right = Node(int(vals[i]))
                q.append(node.right)
            i += 1
        return root
    