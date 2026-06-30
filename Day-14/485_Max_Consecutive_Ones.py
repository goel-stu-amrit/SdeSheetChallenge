class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCon = 0
        count = 0
        for i in nums:
            if i == 1:
                count+=1
                maxCon = max(maxCon, count)
            else:
                count = 0
        return maxCon