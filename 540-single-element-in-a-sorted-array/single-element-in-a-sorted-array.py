class Solution(object):
    def singleNonDuplicate(self, nums):
        n=len(nums)
        low=0
        high=n-1
        if(n>1):

            while low<=high:
                if(nums[low]!=nums[low+1]):
                    return nums[low]
                elif(nums[high]!=nums[high-1]):
                    return nums[high]
                else:
                    low=low+2
                    high=high-2
        
        else:
            return nums[0]     
        """
        :type nums: List[int]
        :rtype: int
        """
        