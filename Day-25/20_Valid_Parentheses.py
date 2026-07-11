class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        mapping = {'}' : "{", ")" : "(", "]": "["}
        for i in s:
            if not stack and i in ")}]":
                return False
            
            if i in mapping:
                top = stack[-1]
                if mapping[i] == top:
                    stack.pop()
                else: return False
            else:
                stack.append(i)
        return not stack