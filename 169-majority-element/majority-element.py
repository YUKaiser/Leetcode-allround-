class Solution(object):
    def majorityElement(self, nums):
        d={}
        for i in range(len(nums)):
            d[nums[i]]=d.get(nums[i],0)+1
        max_key = max(d, key=d.get)
        return max_key
        