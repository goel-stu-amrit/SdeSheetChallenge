# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        nodeInfo = []
        def dfs(node, x, y):
            if not node:
                return
            dfs(node.left, x-1, y-1)
            nodeInfo.append((x, y, node.val))
            dfs(node.right, x+1, y-1)

        dfs(root,0,0)
        nodeInfo.sort(key=lambda t: (t[0], -t[1],t[2]))
        ans = {}
        for x, y, val in nodeInfo:
            if x not in ans:
                ans[x] = []
            ans[x].append(val)
        return [ans[x] for x in sorted(ans)]