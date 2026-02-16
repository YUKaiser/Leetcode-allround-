class Solution(object):
    def searchRange(self, nums, target):
        left=-1
        right=-1
        n=len(nums)
        for i in range (0,n):
            if(nums[i]==target):
                if(left==-1):
                    left=i
                right=i
        return [left,right]
        
       
            
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        