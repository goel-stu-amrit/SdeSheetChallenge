class Solution:
    def trap(self, heights: List[int]) -> int:
        n = len(heights)
        left, right =0, n-1
        leftMax, rightMax = heights[0], heights[right]
        water = 0
        while left < right:
            if leftMax <= rightMax:
                water += leftMax - heights[left]
                left+=1
                leftMax = max(leftMax, heights[left])
            else:
                water += rightMax- heights[right]
                right-=1
                rightMax = max(rightMax, heights[right])
        return water