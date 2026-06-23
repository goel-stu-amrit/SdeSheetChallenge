class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return n
        maxCount = 0
        numset = set(nums)
        for i in numset:
            if i-1  not in numset:
                num = i
                count = 1
                while num+1 in numset:
                    num+=1
                    count+=1
                maxCount = max(count, maxCount)
        return maxCount
