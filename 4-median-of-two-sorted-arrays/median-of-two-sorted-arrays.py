class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res=nums1+nums2
        res.sort()
        n=len(res)
        if n%2!=0:
            return float(res[n//2])
        else:
            return (res[n//2]+res[(n//2)-1])/2.0
            
         