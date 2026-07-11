class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stk=[]
        final=[-1]*len(nums1)
        for i in range(len(nums2)-1,-1,-1):
            while stk and nums2[i]>stk[-1]:
                stk.pop()
            if nums2[i] in nums1:
                if stk:
                    final[nums1.index(nums2[i])]=stk[-1]
                else:
                    final[nums1.index(nums2[i])]=-1
            stk.append(nums2[i])
        return final