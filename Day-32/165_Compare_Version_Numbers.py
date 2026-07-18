class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        n, m = len(v1), len(v2)
        a = max(n, m)
        for i in range(a):
            n1 = v1[i] if i < n else 0
            n2 = v2[i] if i < m else 0
            if n1 < n2: return -1
            if n1 > n2: return 1
        return 0 