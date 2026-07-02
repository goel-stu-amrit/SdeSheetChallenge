class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i, j, count = 0, 0, 0
        m,n = len(g), len(s)
        while i < m and j < n:
            if g[i] <= s[j]:
                count+=1
                i+=1
                j+=1
            else:
                j+=1
        return count
        