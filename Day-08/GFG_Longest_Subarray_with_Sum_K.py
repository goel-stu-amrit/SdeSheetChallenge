class Solution:
    def longestSubarray(self, arr, k):  
        n = len(arr)
        obj = {}
        preSum = 0
        maxLen = 0
        for i in range(n):
            preSum += arr[i]
            if preSum == k:
                maxLen = max(maxLen, i+1)
            rem = preSum -k
            if rem in obj:
                lenSub = i - obj[rem]
                maxLen = max(maxLen, lenSub)
            if preSum not in obj:
                obj[preSum] = i
        return maxLen