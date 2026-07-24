class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        mini=float('inf')
        i=0
        j=0
        sumi=0
        while j<n:
            sumi+=nums[j]
            
            while sumi>=target:
                mini=min(mini,j-i+1)
                sumi-=nums[i]
                i+=1
            
            
            j+=1
        if mini==float('inf'):
            return 0
        return mini
        