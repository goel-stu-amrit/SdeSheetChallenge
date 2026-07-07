class Solution:
    def findPages(self, arr, k):
        n = len(arr)
        if k > n:return -1

        low = max(arr)
        high = sum(arr)

        def canAllocate(limit):
            students = 1
            pages = 0
            for book in arr:
                if pages + book <= limit:
                    pages += book
                else:
                    students += 1
                    pages = book
            return students <= k

        while low <= high:
            mid = (low + high) // 2

            if canAllocate(mid):
                high = mid - 1
            else:
                low = mid + 1

        return low