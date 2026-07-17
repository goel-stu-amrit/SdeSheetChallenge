class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        s = needle + "$" + haystack
        n, m = len(s), len(needle)
        lps = [0] *n
        for i in range(1,n):
            j = lps[i-1]
            if s[j] == s[i]: lps[i] = j+1
            else:
                while j > 0 and s[i] != s[j]:
                    j = lps[j-1]
                if s[i] == s[j]: lps[i] = j+1
            if lps[i] == m:  return i- 2*m
        return -1