class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        low=0
        high=n-1
        lower=-1
        higher=-1
        while low<=high:
            mid=(low+high)//2
            if target<=nums[mid]:
                if target==nums[mid]:
                    lower=mid
                high=mid-1
            else:
                if target==nums[mid]:
                    lower=mid
                low=mid+1
        
        n=len(nums)
        low=0
        high=n-1
        
        while low<=high:
            mid=(low+high)//2
            if target>=nums[mid]:
                if target==nums[mid]:
                    higher=max(mid,higher)
                low=mid+1
            else:
                if target==nums[mid]:
                    higher=max(mid,higher)
                high=mid-1
        return [lower,higher]