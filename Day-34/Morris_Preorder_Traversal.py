class Solution(object):
    def preorderTraversal(self, root):
        #Morris Preorder Traversal
        preorder = []
        curr = root
        while curr:
            if not curr.left:
                preorder.append(curr.val)
                curr = curr.right
            else:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right

                if prev.right==None:
                    prev.right = curr
                    preorder.append(curr.val)
                    curr = curr.left
                else:
                    prev.right = None
                    curr = curr.right
        return preorder