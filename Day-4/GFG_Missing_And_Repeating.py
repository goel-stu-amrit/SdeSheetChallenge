class Solution:
    def findTwoElement(self, arr):
        # code here
        dup = -1
        n = len(arr)
        for i in range(n):
            idx = abs(arr[i]) -1
            
            if arr[idx] < 0:
                dup = abs(arr[i])
            else:
                arr[idx] *= -1
            
        missing = -1
        for i in range(n):
            if arr[i] > 0:
                missing = i+1
                break
            
        return [dup, missing]