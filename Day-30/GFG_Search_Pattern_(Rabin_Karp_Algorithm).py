class Solution:
    def rabinKarp(self, text, pattern):
        if text == pattern: return [0]
        base = 31
        mod = 10**9 + 7

        n = len(text)
        m = len(pattern)

        if m > n:
            return []

        power = pow(base, m - 1, mod)

        p_hash = 0
        t_hash = 0

        # Initial hashes
        for i in range(m):
            p_hash = (p_hash * base + (ord(pattern[i]) - ord('a') + 1)) % mod
            t_hash = (t_hash * base + (ord(text[i]) - ord('a') + 1)) % mod

        ans = []

        for i in range(n - m + 1):

            if p_hash == t_hash:
                if text[i:i + m] == pattern:
                    ans.append(i)

            if i < n - m:
                left = ord(text[i]) - ord('a') + 1
                right = ord(text[i + m]) - ord('a') + 1

                t_hash = (t_hash - left * power) % mod
                t_hash = (t_hash * base + right) % mod

        return ans