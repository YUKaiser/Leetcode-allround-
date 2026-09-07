class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=0
        dicta={}
        for i in range(len(nums)):
            dicta[nums[i]]=dicta.get(nums[i],0)+1
            if maxi<dicta[nums[i]]:
                maxi=dicta[nums[i]]
                a=nums[i]
        return a