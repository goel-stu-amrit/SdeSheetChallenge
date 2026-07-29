class Solution:
    def findPreSuc(self, root, key):
        pre = suc = None
        curr = root
        
        while curr:
            if curr.data > key:
                suc = curr
                curr = curr.left
            elif curr.data < key:
                pre = curr
                curr = curr.right
            else:
                if curr.right:
                    temp = curr.right
                    while temp.left:
                        temp = temp.left
                    suc = temp
                if curr.left:
                    temp = curr.left
                    while temp.right:
                        temp = temp.right
                    pre = temp
                break
        return [pre,suc]