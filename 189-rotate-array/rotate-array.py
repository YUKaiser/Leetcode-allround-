class Solution(object):
    def rotate(self, nums, k):
        new_nums=[0] * len(nums)
        n=len(nums)
        for i in range(n):
                new_nums[(i+k)%n]=nums[i]
        
        for j in range(n):
            nums[j]=new_nums[j]
        
                
        
        