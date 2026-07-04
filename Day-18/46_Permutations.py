class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def recursion(idx, arr):
            if len(arr) == n:
                result.append(arr[:])
                return
            for i in range(idx, n):
                [nums[idx], nums[i]] = [nums[i], nums[idx]]
                recursion(idx+1, arr+[nums[idx]])
                [nums[idx], nums[i]] = [nums[i], nums[idx]]
        recursion(0, [])
        return result