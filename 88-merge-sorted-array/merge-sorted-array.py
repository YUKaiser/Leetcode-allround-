class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        index=m+n-1
        left=m-1
        right=n-1
        while left>=0 and right>=0:
            if nums1[left]<=nums2[right]:
                nums1[index]=nums2[right]
                index-=1
                right-=1
            else:
                nums1[index]=nums1[left]
                index-=1
                left-=1
        while right>=0:
            nums1[index]=nums2[right]
            index-=1
            right-=1
        return nums1