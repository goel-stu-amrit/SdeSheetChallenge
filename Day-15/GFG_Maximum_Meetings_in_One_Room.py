class Solution:
    def maxMeetings(self, s, f) :
        if not s: return []
        arr = []
        n = len(s)
        for i in range(n):
            arr.append((f[i], s[i], i+1))
        arr.sort(key=lambda x: (x[0], x[2]))
        lastEnd = arr[0][0] 
        ans= [arr[0][2]]
        
        for e,s,post in arr[1:]:
            if s > lastEnd:
                ans.append(post)
                lastEnd = e
        ans.sort()
        return  ans