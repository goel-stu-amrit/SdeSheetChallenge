"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""
from collections import deque
class Solution:
    def paths(self, root):
        ans = []
        path = []
        
        def dfs(node):
            if not node:
                return
            path.append(node.data)
            if not node.left and not node.right:
                ans.append(path[:])
            else:
                dfs(node.left)
                dfs(node.right)
            path.pop()
        
        dfs(root)
        return ans