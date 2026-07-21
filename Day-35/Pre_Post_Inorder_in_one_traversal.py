# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        # Pre, Post, Inorder in one traversal
        stack, inorder, preorder, postorder = [], [], [], []
        if not root: return inorder
        stack.append((root, 1))
        while stack:
            node, num = stack.pop()
            if num == 1:
                preorder.append(node.val)
                stack.append((node, num+1))
                if node.left : stack.append((node.left, 1))
            if num == 2:
                inorder.append(node.val)
                stack.append((node, num+1))
                if node.right: stack.append((node.right, 1))
            if num == 3:
                postorder.append(node.val)
        return inorder