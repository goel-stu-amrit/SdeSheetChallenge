class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj = defaultdict()
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if target-num in obj:
                return [i, obj[target-num]]
            obj[num] = i