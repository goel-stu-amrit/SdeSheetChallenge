class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        items = []

        for i in range(len(val)):
            items.append((val[i] / wt[i], val[i], wt[i]))

        items.sort(reverse=True)

        ans = 0.0

        for ratio, value, weight in items:
            if capacity >= weight:
                ans += value
                capacity -= weight
            else:
                ans += ratio * capacity
                break

        return round(ans, 6)
        