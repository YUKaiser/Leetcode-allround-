class Solution(object):
    def findPeakElement(self, nums):
        for i in range (len(nums)):
            if((i==0 or nums[i]>nums[i-1]) and (i==len(nums)-1 or nums[i]>nums[i+1])):
                return i
        
       

      
      
              
        """
        :type nums: List[int]
        :rtype: int
        """
        