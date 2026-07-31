class Solution(object):
    def maxSumBST(self, root):
        self.ans = 0
        def helper(node):
            if not node:
                return (True, float("inf"), float("-inf"), 0)
            lBST, lMin, lMax, lSum = helper(node.left)
            rBST, rMin, rMax, rSum = helper(node.right)
            if lBST and rBST and lMax < node.val < rMin:
                currSum = lSum + rSum + node.val
                self.ans = max(self.ans, currSum)
                
                return (True, min(lMin, node.val), max(rMax, node.val), currSum)
            return (False, 0, 0, 0)

        helper(root)
        return self.ans