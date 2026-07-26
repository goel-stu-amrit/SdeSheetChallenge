class Solution(object):
    def buildTree(self, inorder, postorder):
        obj = {}
        n = len(inorder)
        for i in range(n):
            obj[inorder[i]] = i
        def recursion(sti, edi, stp, edp):
            if sti>edi or stp>edp: return None
            rootval = postorder[edp]
            root = TreeNode(rootval)
            rooti = obj[rootval]
            numleft =  rooti-sti
            root.left = recursion(sti, rooti-1, stp, stp+numleft-1)
            root.right = recursion(rooti+1, edi, stp+numleft, edp-1)
            return root
        return recursion(0, n-1, 0, n-1)