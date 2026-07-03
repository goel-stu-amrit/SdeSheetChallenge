class Solution:
    def palPartition(self, s):
        n = len(s)
        dp = [-1] *n 
        
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]: 
                    return False
                i+=1
                j-=1
            return True
        def f(i):
            if i == n: return 0
            if dp[i] != -1 : return dp[i]
            minCost = n
            for j in range(i, n):
                if isPalindrome(i, j):
                    cost = 1 + f(j+1)
                    minCost = min(cost, minCost)
            dp[i] = minCost
            return minCost
        return f(0)-1
        