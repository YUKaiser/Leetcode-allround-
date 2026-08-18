class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicta={}
        for i in range(len(nums)):
            dicta[nums[i]]=dicta.get(nums[i],0)+1
        
        res=[]
        for a in dicta:
            res.append(dicta[a])
        maxi=max(res)
        a=res.count(maxi)
        return maxi*a
        
        
           