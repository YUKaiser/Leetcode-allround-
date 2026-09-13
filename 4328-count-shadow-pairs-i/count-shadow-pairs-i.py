from bisect import bisect_left
class Solution(object):
    def shadowPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt=0
        stk=[]
        
        for i in range(len(nums)):
            while stk and nums[i]<stk[-1]:
                stk.pop()
            #if stk and nums[i]>stk[-1]:
            cnt+=bisect_left(stk,nums[i])
            
            
            stk.append(nums[i])
        return cnt
        