class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        ans = nums[0]
        for i in nums[1:]:
            curr = max(i, curr+i)
            ans = max(ans, curr)
        return ans 