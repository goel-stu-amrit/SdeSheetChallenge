class Solution:
    def findCeil(self,root, x):
        ceil = -1
        curr = root
        while curr:
            if curr.data == x: return x
            elif curr.data < x: curr = curr.right
            else:
                ceil = curr.data
                curr = curr.left
        return ceil