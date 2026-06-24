from collections import defaultdict

class Solution:
    def subarrayXor(self, arr, k):
        # code here
        obj = defaultdict(int)
        XR = 0
        count = 0
        obj[XR] = 1
        n = len(arr)
        for i in range(n):
            XR ^= arr[i]
            x = XR ^ k
            count += obj[x]
            obj[XR]+=1
        return count