class Solution(object):
    def subArrayRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi=float("-inf")
        mini=float("inf")
        range_s=0
        for i in range(len(nums)):
            maxi=nums[i]
            mini=nums[i]
            for j in range(i,len(nums)):
                maxi=max(maxi,nums[j])
                mini=min(mini,nums[j])
                range_s+=(maxi-mini)
        return range_s        