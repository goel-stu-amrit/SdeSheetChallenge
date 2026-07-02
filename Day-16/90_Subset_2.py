class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)
        def backtrack(idx, arr):
            ans.append(arr[:])
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                backtrack(i+1, arr+[nums[i]])

        backtrack(0, [])        
        return ans
        