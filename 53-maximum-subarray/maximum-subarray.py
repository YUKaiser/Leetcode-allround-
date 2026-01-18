class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        
        maxi=float('-inf')
        totalsum=0
        for j in range(0,n):
            totalsum=nums[j]+totalsum
            maxi=max(maxi,totalsum)
            if totalsum <0:
                totalsum=0
                
        return maxi

        """
        :type nums: List[int]
        :rtype: int
        """
        