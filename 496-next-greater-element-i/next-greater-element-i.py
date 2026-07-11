class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        final=[-1]*len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in nums2:

                a=nums2.index(nums1[i])

                for j in range(a,len(nums2)):
                    if nums1[i]<nums2[j]:
                        final[i]=nums2[j]
                        break
            
        return final
