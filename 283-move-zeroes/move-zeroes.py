class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        position=0
        for i in range(n):
            if (nums[i]!=0):
                nums[position]=nums[i]
                position=position+1
        
        while position<n:
            nums[position]=0
            position=position+1

        
        
