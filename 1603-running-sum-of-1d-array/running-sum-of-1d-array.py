class Solution(object):
    def runningSum(self, nums):
        if(len(nums)==0):
            return []
        psm=[0]*len(nums)
        psm[0]=nums[0]
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
        return nums
      