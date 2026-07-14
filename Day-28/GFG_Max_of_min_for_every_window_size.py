class Solution:
    def maxOfMins(self, arr):
        n = len(arr)
        stack = []
        maxWin = [0]*(n+1)
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                element = stack.pop()
                nse = i
                pse = stack[-1] if stack else -1
                winSize = nse-pse-1
                maxWin[winSize] = max(maxWin[winSize], arr[element])
            stack.append(i)
        while stack:
            element = stack.pop()
            nse = n
            pse = stack[-1] if stack else -1
            winSize = nse-pse-1
            maxWin[winSize] = max(maxWin[winSize], arr[element])
        
        for i in range(n-1, 0, -1):
            maxWin[i] = max(maxWin[i], maxWin[i+1])
        
        return maxWin[1:]
