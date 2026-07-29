class Solution(object):
    def isValidBST(self, root):
        maxval = float("inf")
        def valid(node, minv, maxv):
            if not node: return True
            if node.val <= minv or node.val >= maxv: return False
            return valid(node.left, minv, node.val) and valid(node.right, node.val, maxv)
        
        return valid(root, -maxval, maxval)