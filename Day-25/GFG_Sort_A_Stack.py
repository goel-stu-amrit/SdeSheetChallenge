class Solution:
    def sortStack(self, st):
        
        def insert(stack, val):
            if not stack or stack[-1]<= val:
                stack.append(val)
                return
            temp = stack.pop()
            insert(stack, val)
            stack.append(temp)
                
        def sortStack(stack):
            if not stack:
                return
            temp = stack.pop()
            sortStack(stack)
            insert(stack, temp)
        
        sortStack(st)
        return st