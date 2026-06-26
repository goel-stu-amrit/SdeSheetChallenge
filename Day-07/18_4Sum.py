class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = []
        nums.sort()
        for i in range(n):
            if i>0 and nums[i-1] == nums[i]: continue
            for j in range(i+1, n):
                if j>i+1 and nums[j-1] == nums[j]: continue
                left, right = j+1, n-1
                while(left < right):
                    expectedSum = nums[i]+ nums[j]+ nums[left]+ nums[right]
                    if expectedSum > target:
                        right-=1
                    elif expectedSum < target:
                        left+=1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left+=1
                        right-=1
                        while left < right and nums[left] == nums[left-1]: left+=1
                        while left < right and nums[right] == nums[right+1]: right-=1
        return result