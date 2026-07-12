class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stk=[]
        nums1=nums+nums
        dicta={}
        for i in range(len(nums1)-1,-1,-1):
            while stk and nums1[i]>=stk[-1]:
                stk.pop()
            if stk:
                dicta[i]=stk[-1]
            else:
                dicta[i]=-1
            stk.append(nums1[i])
        final=[0]*len(nums)
        for j in range(len(nums)):
            final[j]=dicta[j]
        return final
        