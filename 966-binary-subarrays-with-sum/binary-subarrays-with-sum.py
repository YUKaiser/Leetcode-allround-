class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        sums=0
        res=0
        dicta={}
        dicta[0]=1
        for i  in range(len(nums)):
            sums+=nums[i]
            if (sums-goal) in dicta:
                res+=dicta.get(sums-goal)
            dicta[sums]=dicta.get(sums,0)+1
        return res