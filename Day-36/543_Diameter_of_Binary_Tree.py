class Solution(object):
    def diameterOfBinaryTree(self, root):
        dia = [0]
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            dia[0] = max(dia[0], left+right)
            return 1 + max(left, right)
        dfs(root)
        return dia[0]