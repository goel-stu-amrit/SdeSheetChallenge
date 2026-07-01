class Solution:
    def jobSequencing(self, deadline, profit):
        jobs = []
        n = len(deadline)
        maxDeadline = 0
        for i in range(n):
            jobs.append((profit[i], deadline[i]))
            if deadline[i] > maxDeadline:
                maxDeadline = deadline[i]
        jobs.sort(reverse = True)
        count =0
        totalProfit = 0
        parent = [i for i in range(maxDeadline + 1)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for p, d in jobs:
            slot = find(d)

            if slot > 0:
                count += 1
                totalProfit += p
                parent[slot] = find(slot - 1)
        return [count, totalProfit]