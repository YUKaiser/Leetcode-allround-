class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stk=[]
        dicta={}
        for i in range(len(nums2)-1,-1,-1):
            while stk and nums2[i]>stk[-1]:
                stk.pop()
            if stk:
                dicta[nums2[i]]=stk[-1]
            else:
                dicta[nums2[i]]=-1
            stk.append(nums2[i])

        final=[]
        for num in nums1:
            final.append(dicta[num])
        return final