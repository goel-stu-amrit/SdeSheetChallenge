class Solution:
    def wordBreak(self, s, dictionary):
        n = len(s)
        wordSet = set(dictionary)
        dp = [-1] * len(s)

        def recursion(idx):
            if idx == n:
                return True
            if dp[idx] != -1:
                return dp[idx]

            for i in range(idx, n):
                if s[idx:i + 1] in wordSet:
                    if recursion(i + 1):
                        dp[idx] = True
                        return True
            dp[idx] = False
            return False

        return recursion(0)