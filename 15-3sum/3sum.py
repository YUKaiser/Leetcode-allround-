class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        n=len(nums)
        res=set()
        for i in range(n):
            dicta=dict()
            for j in range(i+1,n):
                
                a=-(nums[i]+nums[j])
                if a not in dicta:
                    dicta[nums[j]]=True
                else:
                    b=[nums[i],nums[j],a]
                    b.sort()
                    res.add(tuple(b))
        return list(res)