class Solution:
    def romanToInt(self, s: str) -> int:
        romans = { "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000}
        res, n = 0, len(s)
        for i in range(n):
            if i+1 <n and romans[s[i]] < romans[s[i+1]]:
                res-=romans[s[i]]
            else:
                res+=romans[s[i]]
        return res
