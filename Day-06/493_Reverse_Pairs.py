class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        def mergeSort(low, high):
            cnt = 0
            if low >= high: return 0
            mid = (low+high) //2 
            cnt += mergeSort(low, mid)
            cnt += mergeSort(mid+1, high)
            cnt += countPairs(low, mid, high)
            merge(low, mid, high)
            return cnt
            
        def merge(low, mid, high):
            j, k = low, mid+1
            temp = []
            while j<= mid and k<=high:
                if nums[j] < nums[k]:
                    temp.append(nums[j])
                    j+=1
                else:
                    temp.append(nums[k])
                    k+=1
            while j <= mid:
                temp.append(nums[j])
                j+=1
            while k <= high:
                temp.append(nums[k])
                k+=1
            for i in range(low, high+1):
                nums[i] = temp[i-low]

        def countPairs(low, mid, high):
            right = mid+1
            cnt = 0
            for i in range(low, mid+1):
                while(right <= high and  nums[i] > 2*nums[right]): right+=1
                cnt+= right-(mid+1)
            return cnt

        return mergeSort(0, n-1)
        