class Solution:
    def treeToDLL(self, root):
        
        def inorder(node, prev, head):
            if not node: return (prev, head)
            prev, head = inorder(node.left, prev, head)
            if not prev: head = node
            else:
                node.left = prev
                prev.right = node
            prev = node
            prev, head = inorder(node.right, prev, head)
            return prev, head
        
        prev, head = inorder(root, None, None)
        return head