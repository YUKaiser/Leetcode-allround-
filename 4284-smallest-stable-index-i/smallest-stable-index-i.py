class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        maxi=float('-inf')
        for i in range(len(nums)-1):
            maxi=max(maxi,nums[i])
            mini=min(nums[i:len(nums)])
            if maxi-mini<=k:
                return i
        if maxi-nums[-1]<=k:
            return len(nums)-1
        else:
            return -1