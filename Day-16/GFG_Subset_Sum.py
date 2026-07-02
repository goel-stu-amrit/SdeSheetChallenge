class Solution:
	def subsetSums(self, arr):
		# code here
		ans = []
		n = len(arr)
		def backtrack(idx, curSum):
		    if idx == n:
		        ans.append(curSum)
		        return
		    backtrack(idx +1, curSum + arr[idx])
		    backtrack(idx+1, curSum)
		
		backtrack(0,0)
		return ans