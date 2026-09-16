class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res=-1
        low1=0
        high1=nums.index(min(nums))
        res=self.bsearch(nums,target,low1,high1-1)
        low2=high1
        high2=len(nums)-1
        if res==-1:
            res=self.bsearch(nums,target,low2,high2)
        return res
    def bsearch(self,nums,target,low,high):

        while low<=high:
            mid=(low+high)//2
            if target==nums[mid]:
                return mid

            if target<nums[mid]:
                high=mid-1
            else:
                low=mid+1
        return -1