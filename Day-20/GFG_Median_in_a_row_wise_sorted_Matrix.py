class Solution:
    def median(self, mat):
    	n, m= len(mat), len(mat[0])
    	low, high = 3000, 0
    	
    	def blackBox(a):
            count = 0
            for i in range(n):
                if mat[i][0]  <= a:
                    count+= upperBound(i, a)
            return count
            
        def upperBound(row, val):
            low, high = 0, m-1
            ans = m
            while low <= high:
                mid = (low+high)//2
                if mat[row][mid] > val:
                    ans = mid
                    high = mid-1
                else:
                    low = mid+1
            return ans
                        
    	for i in range(n):
    	    low = min(low, mat[i][0])
    	    high = max(high, mat[i][m-1])
    	
    	req = (m*n)//2
    	while low <= high:
    	    mid = (low+high)//2
    	    num = blackBox(mid)
    	    if num <= req:
    	        low = mid+1
            else:
                high = mid-1
        return low