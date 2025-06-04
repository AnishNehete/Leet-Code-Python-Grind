class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = sorted(nums1+ nums2)
        n = len(num)

        if n% 2 == 0:
            mid1 = num[n//2 -1]
            mid2 = num[n//2]
            med = (mid1 + mid2)/2
        else:
            med = num[n//2]
        return med
        #not optimal solution but iiwii