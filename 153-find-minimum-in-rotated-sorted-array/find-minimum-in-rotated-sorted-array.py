class Solution(object):
    def findMin(self, nums):
       low=nums.index(min(nums))
       n=len(nums)
       high=n-1
       while low<=high:
        mid=(low+high)//2
        if(nums[mid]==min(nums)):
            return nums[mid]
        else:
            high=mid-1
        """
        :type nums: List[int]
        :rtype: int
        """
        