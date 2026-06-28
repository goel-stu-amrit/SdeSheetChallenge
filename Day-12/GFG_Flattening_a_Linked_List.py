class Solution:
    def flatten(self, root):
        if not root or not root.next:
            return root
        
        def merge(a,b):
            dummy = Node(-1)
            res = dummy
            while a and b:
                if a.data > b.data:
                    res.bottom = b
                    b = b.bottom
                else:
                    res.bottom = a
                    a = a.bottom
                res = res.bottom
                res.next = None
            if a:
                res.bottom = a
            else:
                res.bottom = b
            return dummy.bottom
        
        return merge(root, self.flatten(root.next)) 