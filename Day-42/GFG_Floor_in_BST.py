class Solution:
    def findMaxFork(self, root, k):
        floor = -1
        curr = root
        while curr:
            if curr.data == k: return curr.data
            elif curr.data > k: curr = curr.left
            else:
                floor = curr.data
                curr = curr.right
        return floor