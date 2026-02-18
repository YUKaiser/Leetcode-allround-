class Solution(object):
    def search(self, nums, target):
        r=-1
        for i in range(0,len(nums)):

            if(nums[i]==target):
                r=i
                return r
        return r
       
     