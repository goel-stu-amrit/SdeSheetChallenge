class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0:
            x = 1/x
            n = -n

        def power (x, n):
            if n == 0: return 1
            halfpow = n//2
            halfval = power(x, halfpow)
            if n%2 == 0:
                return halfval * halfval
            return halfval * halfval * x 
        
        return power(x, n)
# Time Complexity: O(log(n))
# Space Complexity: O(log(n)) due to recursive stack space