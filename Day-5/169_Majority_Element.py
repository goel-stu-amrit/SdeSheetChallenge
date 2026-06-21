class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        freq = 1
        n = len(nums)
        for i in range(1, n):
            if nums[i] == candidate:
                freq+=1
            else:
                freq-=1
            if freq == 0:
                candidate = nums[i]
                freq = 1
        return candidate

# Time Complexity: O(n)
# Space Complexity: O(1)