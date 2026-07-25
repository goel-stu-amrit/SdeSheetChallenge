# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root: return []
        flag = True
        q = deque([root])
        res = []
        while True:
            level = []
            size = len(q)
            for i in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if flag: res.append(level)
            else: res.append(level[::-1])
            flag = not flag
            if res[-1] == []: break
        return res[:-1]