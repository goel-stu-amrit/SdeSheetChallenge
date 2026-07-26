# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        obj = {}
        n = len(inorder)
        for i in range(n):
            obj[inorder[i]] = i
        def recursion(stp, edp, sti, edi):
            if stp>edp or sti> edi: return None
            rootval = preorder[stp]
            root = TreeNode(rootval)
            rooti = obj[rootval]
            numleft = rooti-sti
            root.left = recursion(stp+1, stp+numleft, sti, rooti-1)
            root.right = recursion(stp+numleft+1, edp, rooti+1, edi)
            return root

        return recursion(0,n-1, 0, n-1)