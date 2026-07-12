class Solution:
	def nextSmallerEle(self, arr):
	    stack = []
	    n = len(arr)
	    result = [-1] *n
		for i in range(n-1,-1,-1):
		    if not stack:
		        stack.append(arr[i])
	        else:
	            while stack and  stack[-1] >= arr[i]:
	                stack.pop()
	            if stack:
	                result[i] = stack[-1]
                stack.append(arr[i])
        return result