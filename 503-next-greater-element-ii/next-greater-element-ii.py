class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stk=[]
        n=len(nums)
        result=[-1]*n
        for i in range(2*n-1,-1,-1):
            while stk and nums[i%n]>=stk[-1]:
                stk.pop()
            if i<n:
                
                if stk:
                    result[i]=stk[-1]
            stk.append(nums[i%n])

        return result
        