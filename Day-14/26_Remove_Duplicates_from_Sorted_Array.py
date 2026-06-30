class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            nums[k] = nums[i]
            k+=1
        return k
        