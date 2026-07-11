class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGen = {}

        for num in reversed(nums2):
            while stack and stack[-1]<= num:
                stack.pop()

            nextGen[num] =stack[-1] if stack else -1
            stack.append(num)

        return [nextGen[num] for num in nums1]