class Solution(object):
    def singleNonDuplicate(self, nums):
        n=len(nums) 
        if(n>1):

            if(nums[0]!=nums[1]):
                return nums[0]
           
            for i in range(1,n-1):
                if(nums[i]!=nums[i-1] and nums[i]!=nums[i+1]):
                    return nums[i]
            if(nums[n-1]!=nums[n-1-1]):
                return nums[n-1]
        return nums[0]
        """
        :type nums: List[int]
        :rtype: int
        """
        