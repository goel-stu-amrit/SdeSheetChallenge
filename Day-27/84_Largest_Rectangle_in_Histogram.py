class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea, n = 0, len(heights)
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                element = stack.pop()
                nse = i
                pse = -1 if not stack else stack[-1]
                maxArea = max(maxArea, heights[element]*(nse-pse-1))
            stack.append(i)
        
        while stack:
            nse = n
            element = stack.pop()
            pse = -1 if not stack else stack[-1]
            maxArea = max(maxArea, heights[element]*(nse-pse-1))
            
        return maxArea
