class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        if n ==1: return s
        while n > 1:
            temp = ""
            sl, count = len(s), 1
            for i in range(sl-1):
                if s[i] != s[i+1]:
                    temp += str(count)+str(s[i])
                    count = 1
                else: count+=1
            temp += str(count)+str(s[-1])
            s = temp
            n-=1
        return s