class Solution(object):
    def bstFromPreorder(self, preorder):
        i = [0] #index pointer
        def bst(bound):
            if i[0]==len(preorder) or preorder[i[0]] > bound : return
            root = TreeNode(preorder[i[0]])
            i[0]+=1
            root.left = bst(root.val)
            root.right = bst(bound)
            return root
        
        return bst(float('inf'))