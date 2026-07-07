class Solution:
    def aggressiveCows(self, arr, k):
        n = len(arr)
        arr.sort()

        low = 1
        high = arr[-1] - arr[0]

        def canPlace(dist):
            cows = 1
            last = arr[0]

            for i in range(1, n):
                if arr[i] - last >= dist:
                    cows += 1
                    last = arr[i]

            return cows >= k

        while low <= high:
            mid = (low + high) // 2

            if canPlace(mid):
                low = mid+1
            else:
                high = mid - 1

        return high