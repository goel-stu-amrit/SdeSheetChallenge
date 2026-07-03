class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = 1
        nums = []
        for i in range(1,n):
            fact*= i
            nums.append(i)
        nums.append(n)
        ans = ""
        k = k-1
        while True:
            a = k//fact
            ans += str(nums[a])
            nums = nums[:a] + nums[a+1:]
            if len(nums) == 0:
                break
            k = k%fact
            fact//=len(nums)
        return ans