class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        n,m = len(nums1), len(nums2)
        if n > m: return self.findMedianSortedArrays(nums2, nums1)
        low, high = 0, n
        left = (n+m+1)//2
        while(low <= high):
            mid1 = (low+high)//2
            mid2 = left-mid1
            l1, l2 = float("-inf"), float("-inf")
            r1, r2 = float("inf"), float("inf")
            if(mid1 < n): r1=nums1[mid1]
            if mid2 <m: r2 = nums2[mid2]
            if mid1-1 >=0 : l1 = nums1[mid1-1]
            if mid2-1 >=0 : l2 = nums2[mid2-1]
            if l1 <= r2 and l2 <= r1:
                if (n+m)%2 : return max(l1, l2)
                return (max(l1, l2) + min(r1, r2))/2.0
            elif l1 > r2: high = mid1 -1
            else: low = mid1+1