class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        for i, j in intervals[1:]:
            low, high = ans[-1]
            if high < i:
                ans.append([i,j])
            else:
                ans[-1][1] = max(high, j)
        return ans