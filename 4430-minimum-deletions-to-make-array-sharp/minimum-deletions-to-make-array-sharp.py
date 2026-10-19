class Solution(object):
    def minDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        a=0
        cnt=0
        for i in range(1,len(nums)):
            if nums[a]==nums[i]:
                cnt+=1
            a+=1
        return cnt