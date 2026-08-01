class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dicta={}
        sumi=0
        result=0
        dicta[0]=1
        for i in range(len(nums)):
            sumi+=nums[i]
            
            if (sumi-k) in dicta:
                result+=dicta.get(sumi-k)
                
            dicta[sumi]=dicta.get(sumi,0)+1
        return result