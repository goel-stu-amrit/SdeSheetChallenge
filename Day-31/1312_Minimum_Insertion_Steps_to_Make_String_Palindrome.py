class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        def lcs(st1, st2):
            dp = [[0]*(n+1) for _ in range(n+1)]
            for i in range(1,n+1):
                for j in range(1,n+1):
                    if st1[i-1] == st2[j-1]:
                        dp[i][j] = 1+ dp[i-1][j-1]
                    else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            return dp[n][n]

        return n-lcs(s, s[::-1])