class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLen = 0
        strset = set()
        n = len(s)
        for i in range(n):
            while s[i] in strset:
                strset.remove(s[left])
                left+=1
            strset.add(s[i])
            maxLen = max(maxLen, i-left+1)
        return maxLen