class Solution:
    def nthRoot(self, n, m):
        if m == 0: return 0
        if n == 2:
            root = int(m ** 0.5)
            return root if root*root == m else -1
        
        left, right = 1, m
        while left <= right:
            mid = (left+right)//2
            num = mid**n
            if num == m:
                return mid
            elif num > m:
                right = mid-1
            else: left = mid+1
        return -1