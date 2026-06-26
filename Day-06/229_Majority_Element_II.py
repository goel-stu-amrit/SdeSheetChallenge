class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, count2 = 0,0
        el1, el2 = float('-inf'), float('-inf')

        for i in nums:
            if count1 == 0 and i != el2:
                count1, el1 = 1, i
            elif count2 == 0 and i != el1:
                count2, el2 = 1, i
            elif i == el1: count1+=1
            elif i == el2: count2+=1
            else:
                count1-=1
                count2-=1
        count1, count2 = 0, 0
        for i in nums:
            if el1 == i: count1+=1
            elif el2 == i: count2+=1
        ans = []
        mini = (len(nums)//3)+1
        if count1 >= mini: ans.append(el1)
        if count2 >= mini: ans.append(el2)
        return ans