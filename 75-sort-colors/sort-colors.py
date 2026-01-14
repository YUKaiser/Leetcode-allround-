class Solution(object):
    def sortColors(self, nums):
        for i in range(len(nums)):
            curr_index=i
            for j in range(i+1,len(nums)):
                if (nums[i]>nums[j]):
                    curr_index=j
                    a=nums[i]
                    nums[i]=nums[curr_index]
                    nums[curr_index]=a
            
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        