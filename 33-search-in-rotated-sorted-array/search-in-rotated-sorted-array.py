class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dicta={}
        for i in range(len(nums)):
            dicta[nums[i]]=i
        a=sorted(nums)
        res=-1
        low=0
        n=len(nums)
        high=n-1
        while low<=high:
            mid=(low+high)//2
            if target==a[mid]:
                res=dicta[a[mid]]

            if target<a[mid]:
                high=mid-1
            else:
                low=mid+1
        return res