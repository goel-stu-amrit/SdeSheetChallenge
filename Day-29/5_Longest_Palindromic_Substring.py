class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res, resLen = "", 0
        arr= [res, resLen]
        def helper(left, right, arr):
            while( left >=0 and right<n and s[left] == s[right]):
                sLen = right-left+1
                if arr[1] < sLen:
                    arr[1] = sLen
                    arr[0] = s[left : right+1]
                left-=1
                right+=1
        for i in range(n):
            helper(i,i, arr)
            helper(i, i+1, arr)            
        return arr[0]
            