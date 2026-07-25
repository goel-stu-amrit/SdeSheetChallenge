class Solution:
    def boundaryTraversal(self, root):
        res = []
        def isLeaf(node):
            if not node.left and not node.right:
                return True
            return False
            
        def dfs(node):
            if isLeaf(node):
                res.append(node.data)
                return
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
            
        if not isLeaf(root) : res.append(root.data)
        curr = root.left
        while curr:
            if not isLeaf(curr): res.append(curr.data)
            if curr.left: curr = curr.left
            else: curr = curr.right
        
        dfs(root)
        
        temp, curr = [], root.right
        while curr:
            if not isLeaf(curr): temp.append(curr.data)
            if curr.right: curr = curr.right
            else: curr = curr.left
            
        res+= temp[::-1]
        return res