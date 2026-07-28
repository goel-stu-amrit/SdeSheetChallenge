# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        if val == root.val: return root
        curr = root
        while curr:
            if curr.val > val: curr = curr.left
            elif curr.val< val: curr= curr.right
            else: return curr
        return
        