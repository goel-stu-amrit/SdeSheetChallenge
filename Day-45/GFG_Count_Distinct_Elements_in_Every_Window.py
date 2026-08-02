class Solution:
    def countDistinct(self, arr, k):
        freq = {}
        ans = []

        for i in range(k):
            freq[arr[i]] = freq.get(arr[i], 0) + 1

        ans.append(len(freq))

        for i in range(k, len(arr)):
            left = arr[i-k]
            freq[left] -= 1
            if freq[left] == 0:
                del freq[left]

            freq[arr[i]] = freq.get(arr[i], 0) + 1
            ans.append(len(freq))

        return ans
        