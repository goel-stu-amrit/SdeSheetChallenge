class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result=[]
        dq = deque()
        n = len(nums)
        for i in range(n):
            if dq and dq[0] <= i-k:
                dq.popleft()
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
            if k-1 <=i:
                result.append(nums[dq[0]])
        return result