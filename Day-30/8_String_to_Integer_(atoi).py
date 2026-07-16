class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        if not prefix: return ""
        for i in strs:
            while not i.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix: return ""
        return prefix