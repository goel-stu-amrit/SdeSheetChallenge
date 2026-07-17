class Solution:
    def search(self, pat, txt):
        result = []
        s = pat + "$" + txt
        n, m = len(s), len(pat)
        z = [0] *n
        l, r = 0, 0
        for i in range(1, n):
            if i<r:
                z[i] = min(r - i, z[i - l])

            while(i + z[i] < n and s[i + z[i]] == s[z[i]]) : 
                    z[i]+=1
            if i + z[i] > r:
                    l = i
                    r = i+z[i]
            if z[i] == m:
                result.append(i-m-1)
        return result