class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp, minp = prices[0], prices[0]
        profit = 0
        for i in prices:
            if minp > i:
                minp = i
                maxp = i
            if maxp < i:
                maxp = i
            if profit < maxp-minp:
                profit = maxp- minp
        return profit