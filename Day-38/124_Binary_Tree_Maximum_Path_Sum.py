class Solution(object):
    def maxPathSum(self, root):
        maxi = [-float("inf")]
        
        def maximum(node):
            if not node: return 0
            leftmax = max(0, maximum(node.left))
            rightmax = max(0, maximum(node.right))
            maxi[0] = max(maxi[0], leftmax+ rightmax+ node.val)
            return node.val + max(leftmax, rightmax)

        maximum(root)
        return maxi[0]