class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dicta={}
        if k==len(nums):
            return max(nums)
        i=0
        for j in range(k-1,len(nums)):
            for k in range(i,j+1):
                dicta[nums[k]]=dicta.get(nums[k],0)+1
            i+=1
        
        res=-1
        for num in dicta:
            if dicta[num]==1:
                res=max(res,num)
        return res

        