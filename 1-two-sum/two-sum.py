class Solution(object):
    def twoSum(self, nums, target):
       dicta={}
       for i in range(len(nums)):
        a=target-nums[i]
        if( a in dicta):
            return [i,dicta[a]]
        else:
            dicta[nums[i]]=i

                    
       
        