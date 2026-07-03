class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        result = []
        def recursion(idx, tar, arr):
            if tar == 0:
                result.append(arr[:])
                return
            if idx == n:
                return
            num = candidates[idx]
            if tar >= num:
                recursion(idx, tar-num, arr+[num])
            recursion(idx+1, tar, arr)
        recursion(0, target, [])
        return result