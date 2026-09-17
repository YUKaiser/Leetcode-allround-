class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low=0
        n=len(nums)
        high=n-1
        while low<high:
            mid=(low+high)//2
            if nums[high]<nums[mid]:
                low=mid+1
            else:
                high=mid
            
        
        return nums[low]