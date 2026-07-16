class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        maxval= 2**31-1
        minval = maxval+1
        if not s: return 0
        sign, i, n, res = 1, 0, len(s), 0
        if s[0] =="-":
            sign = -1
            i+=1
        elif s[0] == "+": i+=1
        while(i < n):
            if "0" <= s[i] <= "9":
                res = res*10 + int(s[i])
                if sign == 1 and res > maxval: return maxval
                if sign == -1 and res > minval: return -minval
            else: break
            i+=1
        if res == 0: return 0
        else : return sign * res