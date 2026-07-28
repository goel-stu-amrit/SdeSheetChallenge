# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        if not nums: return
        n = len(nums)//2
        root = TreeNode(nums[n])
        root.left = self.sortedArrayToBST(nums[:n])
        root.right = self.sortedArrayToBST(nums[n+1:])
        return root