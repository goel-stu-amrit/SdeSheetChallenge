class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        result = []
        def recursion(idx, tar, arr):
            if tar == 0:
                result.append(arr[:])
                return
            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i-1]: continue
                if candidates[i] > tar: break
                recursion(i+1, tar-candidates[i], arr+[candidates[i]])
        recursion(0, target, [])
        return result
