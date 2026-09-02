class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        a=len(nums)-k
        res=nums[a:]+nums[:a]
        for i in range(len(nums)):
            nums[i]=res[i]
        return nums