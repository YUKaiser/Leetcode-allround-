class Solution(object):
    def singleNumber(self, nums):
        hash_map={}
        for i in range(0,len(nums)):
            hash_map[nums[i]]=hash_map.get(nums[i],0)+1
        
        for ke,value in hash_map.items():
            if value==1:
                return ke
                break      
