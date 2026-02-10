class Solution(object):
    def searchInsert(self, nums, target):
        n=len(nums)
        low=0
        high=(n-1)
        ind=0
        
        while (low<=high):
            mid=(low+high)//2
            if(nums[mid]>=target):
                ind=mid
                high=mid-1
            else:
                low=mid+1
                ind=low
        return ind
                
            
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        